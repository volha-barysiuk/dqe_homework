from datetime import datetime

from ..utils import validators, text_utils
from ..services import file_services


# Post class serves as the parent class for different types of publications (News, Ads, Rumors, etc.).
# It contains common functionality for supported publications:
#   - Attributes: the type of the post; the text with main content of the post.
#   - Methods: text length validation; normalization of text case; formatting text; publishing text into a txt file.
class Post:
    post_type = 'Post'
    post_prompt = '\nEnter text of the post: '

    def __init__(self, text):
        self._text = validators.validate_str(text, text_type='text', length=500)
        self._cur_date = datetime.now()

    # Combine end line specific to each post type
    # There is no end line for the Posts, so it's set to empty string
    def _add_end_line(self):
        return ''

    # Combine and refine text according to required format and add:
    #   - title stating the post type and append it with underscores,
    #   - the main text,
    #   - additional lines specific to each post type
    def _format_post(self):
        title = self.post_type.ljust(20, '_')
        text = text_utils.normalize_text_case(self._text)
        content = [title, text, self._add_end_line(), '\n']
        return '\n'.join(content)

    # Publish post into the file includes:
    #   - adjusting post format
    #   - writing formatted post into the file
    def publish(self, file_path='news_feed.txt'):
        content = self._format_post()
        file_services.write_file(content, file_path)