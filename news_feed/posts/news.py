from .post import Post
from ..utils import validators


# News class inherits from the Post class and represents a News post.
# It extends the base functionality with:
#   - attributes: the city where the news occurred,
#   - methods: formatting end lines, specific to News posts.
class News(Post):
    post_type = 'News'
    post_prompt = '\nEnter the city: '

    def __init__(self, text, city):
        super().__init__(text)
        self._city = validators.validate_str(city, text_type='city', length=50).title()

    # Combine end line in format: "<City>, <Current date in required format>"
    def _add_end_line(self):
        return f'{self._city}, {self._cur_date.strftime('%d/%m/%Y %H.%M')}'
