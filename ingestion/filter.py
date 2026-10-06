from pathlib import Path
import shutil

source = Path('../data/handbook')
destination = Path('../data/cleaned')

#folders chosen based on containing most relevent data
folders = ["content", "data", "static/pdfs", 'static/files/legal']
allowed_types = ['.md', '.pdf', '.xlsx', '.yaml', '.yml']
paths = []

for folder in folders:
    folder = source / folder
    paths.extend(folder.rglob("*"))

files = []
for path in paths:
    if not path.is_file():
        continue

    if path.suffix.lower() not in allowed_types:
        continue

    relative_path = path.relative_to(source)

    if any(part.startswith(".") for part in relative_path.parts):
        continue
    files.append(relative_path)

def copy_files():

    for file in files:
        source_file = source / file
        destination_file = destination / file

        destination_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_file, destination_file)

    return True

print(copy_files())