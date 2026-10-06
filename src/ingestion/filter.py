from pathlib import Path
import shutil

source = Path('../../data/handbook')
destination = Path('../../data/cleaned')

#folders chosen based on containing most relevent data
folders = ["content", "data", "static/pdfs", 'static/files/legal']
allowed_types = ['.md', '.pdf', '.xlsx', '.yaml', '.yml']
paths = []

#adds all possible paths existing in the data repository
for folder in folders:
    folder = source / folder
    paths.extend(folder.rglob("*"))

files = []
for path in paths:
    if not path.is_file(): #removes paths that do not point towards a file
        continue

    if path.suffix.lower() not in allowed_types: #removes unsupported files
        continue

    relative_path = path.relative_to(source) #makes all paths relative

    #removes all hidden folders / documents (starting w ".")
    if any(part.startswith(".") for part in relative_path.parts):
        continue
    files.append(relative_path)

#copies files into target folder, filtering unwanted junk
def copy_files():

    for file in files:
        source_file = source / file
        destination_file = destination / file

        destination_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_file, destination_file)

    return True

print(copy_files())