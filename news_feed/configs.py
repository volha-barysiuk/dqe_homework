from news_feed.posts.news import News
from news_feed.posts.private_ad import PrivateAd
from news_feed.posts.rumor import Rumor

# Default file paths
INPUT_FILE_PATH = 'files/input.txt'
INPUT_JSON_PATH = 'files/input.json'
OUTPUT_FILE_PATH = 'files/newsfeed.txt'
ERROR_FILE_PATH = 'files/errors.txt'
WORDS_COUNT_PATH = 'files/words_count.csv'
LETTERS_COUNT_PATH = 'files/letters_count.csv'

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
OUTPUT_FILE = f'Change output file (default: {OUTPUT_FILE_PATH})'
ERROR_FILE = f'Error file (default: {ERROR_FILE_PATH})'
DEFAULT_FILE = f'Use current input file'
DEFAULT_JSON = f'Use current JSON input file'

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
    [RETURN, INPUT_FILE, INPUT_JSON, DEFAULT_FILE, DEFAULT_JSON],
    [RETURN, INPUT_FILE, INPUT_JSON, OUTPUT_FILE, ERROR_FILE]
]

MENU_DICT = dict(zip(MAIN_MENU, SUB_MENU))