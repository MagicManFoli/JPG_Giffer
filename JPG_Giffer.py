#!python3

from pathlib import Path
from os.path import join

file_extensions = ('*.jpg', '*.jpeg')   # case insensitive


def input_path():
    """encapsulates folder selection"""
    folder_path = Path(input("Input path to folder:\n>"))

    if folder_path == "":
        print("Goodbye")
        exit(0)

    return folder_path


def change_extension(file):
    p = Path(file)
    file_name = p.stem
    base_path = p.parent

    print("Current: {} in {}".format(file_name, base_path))




def main():
    print("Collecting files")

    # folder_path = input_path()
    folder_path = Path("E:\Test")

    files = []

    for ext in file_extensions:
        mask = "**/" + ext
        new_files = list(folder_path.glob(mask))
        print("{} files with {} found".format(len(new_files), ext))
        files.extend(new_files)

    print("{} files found".format(len(files)))

    print("Renaming")

    for file in files:
        change_extension(file)

    print("Done.")

# end of main


if __name__ == "__main__":
    main()
