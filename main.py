import pathlib
import sys
from get_hashes_from_directory import hash_files_in_directory
from check_for_duplicates import delete_duplicates


def main():
    print(f"starting")
    source_directory = pathlib.Path(sys.argv[1])
    target_directory = pathlib.Path(sys.argv[2])
    hashed_files_source = hash_files_in_directory(source_directory)
    hashed_files_target = hash_files_in_directory(target_directory)
    files_to_copy = delete_duplicates(hashed_files_source, hashed_files_target)

    print(f"\n{len(files_to_copy)} files for copying")
    print_items(files_to_copy)


def print_items(dict):
    for item in dict.keys():
        print(f"Item: {item}, hash: {dict[item]}")


if __name__ == "__main__":
    main()


# check file is mp3 or wav
# hash file (I have code for this)
# use that code I have to store hashes and path as a dictionary in target folder, do same for source folder.
# for each hash in source folder dict, check it's not in target folder dict.
# if exact hash is in target folder dict, delete hash and path from source folder dict
# once done, copy all remaining items to target folder.