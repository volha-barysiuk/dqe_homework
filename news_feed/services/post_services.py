from news_feed.configs import CLASSES
from news_feed.posts import news, private_ad, rumor
from news_feed.services.file_services import write_file, read_file, write_csv, write_csv_with_headers
from news_feed.utils.text_utils import count_entity, get_stats


# The create_post function works with post text and additional details based on the post type.
# It creates post based on provided attributes and raises error if attributes are missing or invalid.
def create_post(post_type, text, end_line):
    try:
        return CLASSES.get(post_type)(text, end_line)
    except Exception as e:
        if post_type not in CLASSES:
            e = 'Post type is missing or invalid'
        raise AttributeError(f'Cannot create post using provided data:\n{e}')


def publish_post(post_type, text, end_line, output_file_path, error_file_path, manual=False):
    try:
        post = create_post(post_type, text, end_line)
        post.publish(output_file_path)
        return True
    except Exception as e:
        sep = '=' * 40
        content = '\n'.join([sep, str(e), sep, post_type + ':', text, end_line, '\n\n'])
        write_file(content, error_file_path)
        if manual:
            print(e)
        return False


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
