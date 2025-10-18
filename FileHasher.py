import hashlib

BUFFER_SIZE = 1024

# public
def hash_file(filepath):
    print(f"hashing {filepath}")
    with filepath.open(mode='rb') as file:
        hasher = hashlib.sha1()
        update_hash(hasher, file)
        return hasher.hexdigest()

# private
def update_hash(hasher, file):
    end_of_data = False

    while not end_of_data:
        data = file.read(BUFFER_SIZE)
        end_of_data = is_file_ended(data)
        hasher.update(data)

def is_file_ended(data):
    return True if not data else False