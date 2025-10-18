import pathlib
import sys
import shutil
from get_hashes_from_directory import hash_files_in_directory
from filter_files import delete_duplicates, filter_by_extension


def main():
    print(f"starting")
    source_directory = pathlib.Path(sys.argv[1])
    target_directory = pathlib.Path(sys.argv[2])

    if sys.argv[3]:
        file_extension = sys.argv[3]
    else:
        file_extension = None

    filtered_source_files = filter_by_extension(source_directory, file_extension)
    hashed_files_source = hash_files_in_directory(filtered_source_files)
    hashed_files_target = hash_files_in_directory(target_directory)
    files_to_copy = delete_duplicates(hashed_files_source, hashed_files_target)

    print(f"\n{len(files_to_copy)} files for copying")
    print_items(files_to_copy)

    proceed_answer = input(f"\nProceed? [y/n]")
    if proceed_answer in ["Y", "y", "yes"]:
        copy_files(target_directory, files_to_copy)

    print(f"\nprocess ending")


def print_items(dict):
    for item in dict.keys():
        print(f"Item: {item}, hash: {dict[item]}")


def copy_files(target_directory, files_to_copy):
    for item in files_to_copy:
        print(f"Copying {item}")
        target_file_path = f"{target_directory}/{item.name}"
        shutil.copy(item, target_file_path)
    print(f"\n{len(files_to_copy)} files copied to {target_directory}")

if __name__ == "__main__":
    main()


# check file is mp3 or wav
# hash file (I have code for this)
# use that code I have to store hashes and path as a dictionary in target folder, do same for source folder.
# for each hash in source folder dict, check it's not in target folder dict.
# if exact hash is in target folder dict, delete hash and path from source folder dict
# once done, copy all remaining items to target folder.