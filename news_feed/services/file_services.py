# Write data to the file while handling any unexpected errors that may occur
def write_file(content, file_path):
    try:
        with open(file_path, 'a+', encoding='utf-8') as file:
            file.write(content)
    except FileNotFoundError:
        raise FileNotFoundError(f'File not found at "{file_path}"')
    except Exception as e:
        raise RuntimeError(f'Unexpected error occurred while writing data into "{file_path}": {e}')

# Read data from the file by lines while handling any unexpected errors that may occur
def open_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        raise FileNotFoundError(f'File not found at "{file_path}"')
    except Exception as e:
        raise RuntimeError(f'Unexpected error occurred while reading data from "{file_path}": {e}')