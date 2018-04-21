#!python3

import glob
from pathlib import Path
from os.path import join

file_extensions = ('*.jpg','*.JPG', '*.jpeg', )

def input_path():
    """encapsulates folder selection"""
    while True:
        folder_path = input("Input path to folder:\n>")

        if folder_path == "":
            print("Goodbye")
            exit(0)



        if not file_list:  # empty lists are "False"
            print("no PDFs in that directory, try again")
        else:
            break
    return file_list


def main():
    print("Collecting files")

    folder_path = input_path()

    files = []

    for ext in file_extensions:
        files.extend(glob.glob(join(folder_path, ext), recursive=True))

    print("{} files found".format(files.count()))




# end of main


if __name__ == "__main__":
    main()
