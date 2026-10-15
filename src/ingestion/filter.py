from pathlib import Path
import shutil

source = Path('../../data/handbook')
destination = Path('../../data/cleaned')

#folders chosen based on containing most relevent data
folders = ["content", "data", "static/pdfs", 'static/files/legal']
allowed_types = ['.md', '.pdf', '.xlsx', '.yaml', '.yml']
paths = []

files = []

def filter_files(paths, repo):
    repo = Path(repo).resolve()
    files = []
    for path in paths:
        path = Path(path)
        if not path.is_file(): #removes paths that do not point towards a file
            continue

        if path.suffix.lower() not in allowed_types: #removes unsupported files
            continue

        try:
            relative_path = path.resolve().relative_to(repo)
        except ValueError:
            continue #removes files outside the repository

        #checks only folders / documents inside the repository
        if any(part.startswith(".") for part in relative_path.parts):
            continue

        if not any(relative_path.is_relative_to(Path(folder)) for folder in folders):
            continue
        files.append(path)

    return files

#copies files into target folder, filtering unwanted junk
def copy_files():

    for file in files:
        source_file = file
        relative_path = file.relative_to(source)
        destination_file = destination / relative_path

        destination_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_file, destination_file)

    return True

if __name__ == "__main__":
    for folder in folders:
        paths.extend((source / folder).rglob("*"))
    files = filter_files(paths, source)
    print(copy_files())
