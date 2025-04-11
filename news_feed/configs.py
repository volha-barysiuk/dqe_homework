import os

from .posts.news import News
from .posts.private_ad import PrivateAd
from .posts.rumor import Rumor

# DB connection configs
DB_NAME = 'posts_storage.db'
DB_PATH = os.path.join('news_feed', DB_NAME)
DB_CONN = 'DRIVER={SQLite3 ODBC Driver};DATABASE=' + DB_PATH + ';'

# Default file paths
FILE_PATH = os.path.join('news_feed', 'files')
INPUT_FILE_PATH = os.path.join(FILE_PATH, 'input.txt')
INPUT_JSON_PATH = os.path.join(FILE_PATH, 'input.json')
INPUT_XML_PATH = os.path.join(FILE_PATH, 'input.xml')
OUTPUT_FILE_PATH = os.path.join(FILE_PATH, 'newsfeed.txt')
ERROR_FILE_PATH = os.path.join(FILE_PATH, 'errors.txt')
WORDS_COUNT_PATH = os.path.join(FILE_PATH, 'words_count.csv')
LETTERS_COUNT_PATH = os.path.join(FILE_PATH, 'letters_count.csv')

# Generic menu options
EXIT = 'Exit the program'
RETURN = 'Return to the main menu'

# Main menu options
ENTER_POST = 'Enter post(s) from the terminal'
FILE_UPLOAD = 'Upload post(s) from a file'
FILE_PATHS = 'Change the file paths'

# Posts sub-menu options
NEWS = 'News'
PRIVATE_AD = 'Private Ad'
RUMOR = 'Rumor'

# File sub-menu options
INPUT_FILE = f'Change input file (default: {INPUT_FILE_PATH})'
INPUT_JSON = f'Change input JSON file (default: {INPUT_JSON_PATH})'
INPUT_XML = f'Change input XML file (default: {INPUT_XML_PATH})'
OUTPUT_FILE = f'Change output file (default: {OUTPUT_FILE_PATH})'
ERROR_FILE = f'Error file (default: {ERROR_FILE_PATH})'
DEFAULT_FILE = f'Use current input file'
DEFAULT_JSON = f'Use current JSON input file'
DEFAULT_XML = f'Use current XML input file'

# Post type class mapper
CLASSES = {
    NEWS: News,
    PRIVATE_AD: PrivateAd,
    RUMOR: Rumor,
}

# Menu navigator
MAIN_MENU = [EXIT, ENTER_POST, FILE_UPLOAD, FILE_PATHS]
SUB_MENU = [
    [],
    [RETURN, *CLASSES.keys()],
    [RETURN, INPUT_FILE, INPUT_JSON, INPUT_XML, DEFAULT_FILE, DEFAULT_JSON, DEFAULT_XML],
    [RETURN, INPUT_FILE, INPUT_JSON, INPUT_XML, OUTPUT_FILE, ERROR_FILE]
]

MENU_DICT = dict(zip(MAIN_MENU, SUB_MENU))
