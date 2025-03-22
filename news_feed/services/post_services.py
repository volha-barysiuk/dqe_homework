from news_feed.configs import CLASSES
from news_feed.posts import news, private_ad, rumor
from news_feed.services.file_services import write_file


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


