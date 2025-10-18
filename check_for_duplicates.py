def delete_duplicates(source_dict, target_dict):
    files_to_copy = source_dict.copy()
    for key, value in source_dict.items():
        if value in target_dict.values():
            del files_to_copy[key]

    return files_to_copy