import json
import subprocess
from pathlib import Path

repo = Path('../../data/handbook')

def get_current_commit():

    local_result = subprocess.run(
            ['git', 'rev-parse', 'HEAD'],
            cwd=repo,
            capture_output=True,
            text=True,
            check=True
        )
    
    return local_result.stdout.strip()


def get_remote_commit():
    remote_result = subprocess.run(
            ['git', 'ls-remote', '--exit-code', 'origin', 'refs/heads/main'],
            cwd=repo,
            capture_output=True,
            text=True,
            check=True,
            timeout=30
        )

    return remote_result.stdout.split()[0]
    
def has_remote_changed():

    local_hash = get_current_commit()
    remote_hash = get_remote_commit()
    return local_hash == remote_hash

def sync_data(repo):

    current_commit = get_current_commit()

    if has_remote_changed():
        subprocess.run(
            ['git', 'fetch', 'origin'],
            cwd=repo,
            capture_output=True,
            text=True,
            check=True
        )

        target_commit = subprocess.run(
            ["git", "rev-parse", "origin/main"],
            cwd=repo,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()

        diff_result = subprocess.run(
            [
                "git", "diff",
                "--name-status",
                "--no-renames",
                "-z",
                current_commit,
                target_commit,
                "--",
            ],
            cwd=repo,
            capture_output=True,
            text=True,
            check=True,
        )

        changes = {
            "added": [],
            "modified": [],
            "deleted": [],
        }

        fields = diff_result.stdout.split("\0")

        for i in range(0, len(fields) - 1, 2):
            status = fields[i]
            path = fields[i + 1]

            if status == "A":
                changes["added"].append(path)
            elif status in {"M", "T"}:
                changes["modified"].append(path)
            elif status == "D":
                changes["deleted"].append(path)
            else:
                raise RuntimeError(f"Unexpected status: {status} for {path}")

        subprocess.run(
            ["git", "merge", "--ff-only", target_commit],
            cwd=repo,
            capture_output=True,
            text=True,
            check=True,
        )

        paths_to_load = [
            repo / relative_path
            for relative_path in changes["added"] + changes["modified"]
        ]

        deleted_absolute_paths = [
            repo / relative_path
            for relative_path in changes["deleted"]
        ]

        return {
        "old_commit": current_commit,
        "target_commit": target_commit,
        "changes": {
            "changes": paths_to_load,
            "deletions": deleted_absolute_paths
            }
    }