import shutil

def copy_files(target_directory, files_to_copy):
    for item in files_to_copy:
        print(f"Copying {item}")
        target_file_path = f"{target_directory}/{item.name}"
        shutil.copy(item, target_file_path)
    print(f"\n{len(files_to_copy)} files copied to {target_directory}")