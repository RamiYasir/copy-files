def delete_duplicates(source_dict, target_dict):
    for key, value in source_dict.items():
        if value in target_dict.values():
            del source_dict[key]
    return source_dict