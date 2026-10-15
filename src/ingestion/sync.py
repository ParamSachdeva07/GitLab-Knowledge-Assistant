import json
import subprocess
from pathlib import Path
from langfuse import observe

project_root = Path(__file__).resolve().parents[2]
repo = project_root / "data" / "handbook"


def git(repo, *args):
    return subprocess.run(
        ["git", *args], cwd=repo, capture_output=True,
        text=True, check=True, timeout=120,
    ).stdout.strip()


def get_current_commit(repo=repo):
    return git(repo, "rev-parse", "HEAD")


def get_remote_commit(repo=repo):
    return git(repo, "ls-remote", "--exit-code", "origin", "refs/heads/main").split()[0]


def has_remote_changed(repo=repo):
    return get_current_commit(repo) != get_remote_commit(repo)


def save_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(value, default=str, indent=2), encoding="utf-8")
    temporary.replace(path)


@observe(name="ingestion.git_sync", capture_input=False, capture_output=False)
def sync_data(repo, indexed_commit=None, pending_path=None, full_rebuild=False):
    if git(repo, "status", "--porcelain"):
        raise RuntimeError("Repository has local changes; stop before syncing")

    current_commit = get_current_commit(repo)
    if pending_path is not None and pending_path.exists():
        # Finish the saved target before considering newer upstream commits.
        report = json.loads(pending_path.read_text(encoding="utf-8"))
        if current_commit not in {report["checkout_commit"], report["target_commit"]}:
            raise RuntimeError("Checkout moved while an ingestion run was pending")
    elif full_rebuild:
        # Index the current committed checkout without fetching upstream.
        tracked_paths = subprocess.run(
            ["git", "ls-tree", "-r", "--name-only", "-z", current_commit],
            cwd=repo, capture_output=True, text=True, check=True, timeout=120,
        ).stdout
        paths = [repo / path for path in tracked_paths.split("\0") if path]
        report = {
            "full_rebuild": True,
            "old_commit": indexed_commit,
            "checkout_commit": current_commit,
            "target_commit": current_commit,
            "changes": {"additions": paths, "modifications": [], "deletions": []},
            "file_counts": {"added": len(paths), "modified": 0, "deleted": 0},
            "remaining_deletions": [],
            "remaining_additions": paths,
            "completed_files": {},
        }
        if pending_path is not None:
            save_json(pending_path, report)
    else:
        git(repo, "fetch", "origin")
        target_commit = git(repo, "rev-parse", "origin/main")
        git(repo, "merge-base", "--is-ancestor", current_commit, target_commit)
        old_commit = indexed_commit or current_commit
        fields = git(
            repo, "diff", "--name-status", "--no-renames", "-z",
            old_commit, target_commit, "--",
        ).split("\0")
        changes = {"additions": [], "modifications": [], "deletions": []}
        counts = {"added": 0, "modified": 0, "deleted": 0}
        for i in range(0, len(fields) - 1, 2):
            status, relative_path = fields[i:i + 2]
            if status == "A":
                counts["added"] += 1
            elif status in {"M", "T"}:
                counts["modified"] += 1
            elif status == "D":
                counts["deleted"] += 1
            else:
                raise RuntimeError(f"Unexpected status: {status} for {relative_path}")
            key = "deletions" if status == "D" else "additions" if status == "A" else "modifications"
            changes[key].append(repo / relative_path)

        report = {
            "old_commit": old_commit,
            "checkout_commit": current_commit,
            "target_commit": target_commit,
            "changes": changes,
            "file_counts": counts,
            "remaining_deletions": changes["deletions"] + changes["modifications"],
            "remaining_additions": changes["additions"] + changes["modifications"],
            "completed_files": {},
        }
        # Persist before moving Git, so a crash after merging is recoverable.
        if pending_path is not None:
            save_json(pending_path, report)

    git(repo, "merge-base", "--is-ancestor", current_commit, report["target_commit"])
    git(repo, "merge", "--ff-only", report["target_commit"])
    for key in ("additions", "modifications", "deletions"):
        report["changes"][key] = [Path(path) for path in report["changes"][key]]
    return report
