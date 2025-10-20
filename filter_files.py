def delete_duplicates(source_dict, target_dict):
    files_to_copy = source_dict.copy()
    for key, value in source_dict.items():
        if value in target_dict.values():
            del files_to_copy[key]

    return files_to_copy


def filter_by_extension(source_dict, file_extension):
    files_to_copy = source_dict.copy()
    if file_extension is not None:
        for key in source_dict.keys():
            if not key.suffix.endswith(file_extension):
                del files_to_copy[key]

    return files_to_copy