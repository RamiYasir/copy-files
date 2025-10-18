import pathlib
from hash_files import hash_file

SKIP_DIRS = ["temp", "temporary_files", "logs", ".idea", ".venv"]


def hash_files_in_directory(root):
    print(f"hashing {root}")
    generator = get_all_items(root)
    return get_hashes_as_dict(generator)


def get_all_items(root: pathlib.Path):
    for item in root.iterdir():
        if item.name in SKIP_DIRS:
            continue
        if item.is_dir():
            yield from get_all_items(item)
        else:
            yield item, hash_file(item)


def get_hashes_as_dict(generator):
    hashes_dict = {}
    for iterable in generator:
        key = iterable[0]
        value = iterable[1]
        hashes_dict[key] = value
    return hashes_dict