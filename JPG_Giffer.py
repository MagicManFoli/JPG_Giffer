#!python3

from pathlib import Path

file_extensions = ('*.jpg', '*.jpeg')   # case insensitive


# TODO: Check file header if file is actually a gif

def input_path():
    """encapsulates folder selection"""
    folder_path = Path(input("Input path to folder:\n>"))

    if folder_path == "":
        print("Goodbye")
        exit(0)

    return folder_path


def change_extension(file):
    p = Path(file)
    file_name = p.stem  # file without extension
    base_path = p.parent  # path without file

    print("Current: {} in {}".format(file_name, base_path))
    p.rename(Path(base_path, file_name + "_R.gif"))
    # print("Now called {}".format(p))  # TODO: Why is this showing the old name? Racing with file operation?


def main():
    print("Collecting files")

    folder_path = input_path()

    files = []

    for ext in file_extensions:
        mask = "**/" + ext
        new_files = list(folder_path.glob(mask))  # generator to list, easier but less efficient
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
