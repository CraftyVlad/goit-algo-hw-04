import argparse
import shutil
from pathlib import Path


def copy_files(source, destination):
    try:
        for item in source.iterdir():
            if item.is_dir():
                if item.resolve() != destination.resolve():
                    copy_files(item, destination)
            elif item.is_file():
                extension = item.suffix[1:].lower() or "no_extension"
                folder = destination / extension
                folder.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, folder / item.name)

    except OSError as error:
        print(f"error: {error}")


parser = argparse.ArgumentParser()
parser.add_argument("source")
parser.add_argument("destination", nargs="?", default="dist")
args = parser.parse_args()

source = Path(args.source)
destination = Path(args.destination)

if not source.is_dir():
    print("source directory does not exist!")
elif source.resolve() == destination.resolve():
    print("source and destination must be different!")
else:
    try:
        destination.mkdir(parents=True, exist_ok=True)
        copy_files(source, destination)
        print("copying completed")
    except OSError as error:
        print(f"error: {error}")