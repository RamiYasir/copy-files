import pathlib
import sys
from hash_directory import hash_files_in_directory
from filter_files import delete_duplicates, filter_by_extension
from manipulate_files import copy_files


def main():
    print(f"starting")
    source_directory = pathlib.Path(sys.argv[1])
    target_directory = pathlib.Path(sys.argv[2])

    if len(sys.argv) > 3:
        file_extension = sys.argv[3]
    else:
        file_extension = None

    hashed_files_source = hash_files_in_directory(source_directory)
    hashed_files_target = hash_files_in_directory(target_directory)
    filtered_source_files = filter_by_extension(hashed_files_source, file_extension)
    files_to_copy = delete_duplicates(filtered_source_files, hashed_files_target)

    print(f"\n{len(files_to_copy)} files for copying")
    print_items(files_to_copy)

    proceed_answer = input(f"\nProceed? [y/n]")
    if proceed_answer in ["Y", "y", "yes"]:
        copy_files(target_directory, files_to_copy)

    print(f"\nprocess ending")


def print_items(dict):
    for item in dict.keys():
        print(f"Item: {item}, hash: {dict[item]}")


if __name__ == "__main__":
    main()
