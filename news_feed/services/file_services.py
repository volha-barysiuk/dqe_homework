import csv
import json
import xml.etree.ElementTree as ET

# Function to append the file with provided text and handle any unexpected errors that may occur during file processing.
#   Parameter: file_path (str): The path to the file that needs to be read.
def write_file(content, file_path):
    try:
        with open(file_path, 'a+', encoding='utf-8') as file:
            file.write(content)
    except FileNotFoundError:
        raise FileNotFoundError(f'File not found at "{file_path}"')
    except Exception as e:
        raise RuntimeError(f'Unexpected error occurred while writing data into "{file_path}": {e}')


# Function to read the contents of a file and handle any unexpected errors that may occur during file processing.
#   Parameters:
#   - file_path (str): The path to the file that needs to be read.
#   - read_lines (bool): Flag to determine whether to read the file line by line (True) or as a single string (False). Default is True.
def read_file(file_path, read_lines=True):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines() if read_lines else file.read()
            return lines
    except FileNotFoundError:
        raise FileNotFoundError(f'File not found at "{file_path}"')
    except Exception as e:
        raise RuntimeError(f'Unexpected error occurred while reading data from "{file_path}": {e}')


# Function to write the text into csv file and handle any unexpected errors that may occur during file processing.
#   Parameters:
#   - content (dict): Text to be written, the object of Counter class.
#   - file_path (str): The path to the csv file that needs to be read.
#   - delimiter: Character to separate values in csv file (Default: comma).
def write_csv(content, file_path, delimiter=','):
    try:
        with open(file_path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=delimiter)
            for el in content.items():
                writer.writerow(el)
    except FileNotFoundError:
        raise FileNotFoundError(f'File not found at "{file_path}"')
    except Exception as e:
        raise RuntimeError(f'Unexpected error occurred while writing data into "{file_path}": {e}')


# Function to write the text into csv file with headers and handle any unexpected errors that may occur during file processing.
#   Parameters:
#   - content (dict): Text to be written.
#   - file_path (str): The path to the csv file that needs to be read.
#   - delimiter: Character to separate values in csv file (Default: comma).
def write_csv_with_headers(content, file_path, delimiter=','):
    headers = list(content[0].keys())
    try:
        with open(file_path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers, delimiter=delimiter)
            writer.writeheader()
            writer.writerows(content)
    except FileNotFoundError:
        raise FileNotFoundError(f'File not found at "{file_path}"')
    except Exception as e:
        raise RuntimeError(f'Unexpected error occurred while writing data into "{file_path}": {e}')


# Function to read the contents of a JSON file (the content gets stored as dictionary data type)
# and handle any unexpected errors that may occur during file processing.
#   Parameters:
#   - file_path (str): The path to the JSON file that needs to be read.
def read_json_file(file_path):
    try:
        raw_post_list = json.load(open(file_path, 'r', encoding='utf-8'))
        return raw_post_list
    except FileNotFoundError:
        raise FileNotFoundError(f'File not found at "{file_path}"')
    except Exception as e:
        raise RuntimeError(f'Unexpected error occurred while reading data from "{file_path}": {e}')


# Function to read the contents of an XML file (the content gets stored as etree element)
# and handle any unexpected errors that may occur during file processing.
#   Parameters:
#   - file_path (str): The path to the XML file that needs to be read.
def read_xml_file(file_path):
    try:
        tree = ET.parse(file_path)
        posts_root = tree.getroot()
        return posts_root
    except FileNotFoundError:
        raise FileNotFoundError(f'File not found at "{file_path}"')
    except Exception as e:
        raise RuntimeError(f'Unexpected error occurred while reading data from "{file_path}": {e}')
