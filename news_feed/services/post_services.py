import pyodbc

from ..configs import CLASSES, DB_CONN
from .file_services import write_file, read_file, write_csv, write_csv_with_headers
from ..utils.text_utils import count_entity, get_stats


# The create_post function works with post text and additional details based on the post type.
# It creates post based on provided attributes and raises error if attributes are missing or invalid.
def create_post(post_type, text, end_line):
    try:
        return CLASSES.get(post_type)(text, end_line)
    except Exception as e:
        if post_type not in CLASSES:
            e = 'Post type is missing or invalid'
        raise AttributeError(f'Cannot create post using provided data:\n{e}')


# Function to publish a single post based on user input and store the results in specified output files.
# Additionally, the function stores the posts in the database if no matching posts are found.
# Parameters:
# - post_type (str): Type of the post.
# - text (str): Text (the main content block) of the post.
# - end_line (str): The end line custom for each post type (e.g. city for the news or expiry date for the private ad).
# - output_file_path (str): Path to the output file (e.g., newsfeed.txt) used to store published posts; represents final newsfeed.
# - error_file_path (str): Path to the file used to write the errors occurring while publishing posts.
# - manual (bool): If False (default), errors are printed to the console (suitable for manual input). If True, errors are logged only to the error file.
def publish_post(post_type, text, end_line, output_file_path, error_file_path, manual=False):
    try:
        post = create_post(post_type, text, end_line)
        try:
            with pyodbc.connect(DB_CONN) as conn:
                if post.is_stored_in_db(conn):
                    raise ValueError('Post already exists.')
                post.publish(output_file_path)
                post.store_in_db(conn)
                return True
        except pyodbc.Error:
            raise ValueError('Your post could not be processed due to a database error.')
    except Exception as e:
        sep = '=' * 40
        content = '\n'.join([sep, str(e), sep, post_type + ':', text, end_line, '\n\n'])
        write_file(content, error_file_path)
        if manual:
            print(e)
        return False


# Function to publish multiple posts retrieved from specified input files, and store the results into specified output files.
# Parameters:
# - raw_posts (list): list of data required to create new posts (post type, text, end line custom for each post type)
# - input_file_path (str): Path to the input file that stores raw posts; accepts TXT, JSON, XML files.
# - output_file_path (str): Path to the output file (e.g., newsfeed.txt) used to store published posts; represents final newsfeed.
# - error_file_path (str): Path to the file used to write the errors occurring while publishing posts.
# - words_file_path (str): Path to the CSV file where word count statistics will be stored.
# - letters_file_path (str): Path to the CSV file where letter count statistics will be stored.
def publish_multiple_posts(raw_posts, input_file_path, output_file_path,
                           error_file_path, words_count_file_path, letters_count_file_path):
    for post_type, text, end_line in raw_posts:
        publish_post(post_type, text, end_line, output_file_path, error_file_path)
    print(f'\nThe file {input_file_path} has been processed.')
    print(f'If any errors were encountered, they have been logged to: {error_file_path}.')
    write_stats_to_csv(output_file_path, words_count_file_path, letters_count_file_path)


# Function to calculate the counts of words and letters from the given input file and write the results to separate csv files.
# Parameters:
# - input_file_path (str): Path to the input file (e.g., newsfeed.txt) used to calculate word and letter counts.
# - words_file_path (str): Path to the CSV file where word count statistics will be stored.
# - letters_file_path (str): Path to the CSV file where letter count statistics will be stored.
def write_stats_to_csv(input_file_path, words_file_path, letters_file_path):
    try:
        content = read_file(input_file_path, read_lines=False)
        counted_words = count_entity(content)
        write_csv(counted_words, words_file_path, '-')
        counted_letters = count_entity(content, entity='letter', to_lower=False)
        write_csv_with_headers(get_stats(counted_letters), letters_file_path, ',')
    except Exception as e:
        print(e)
