from news_feed.posts.post import Post
from news_feed.utils import validators


# News class inherits from the Post class and represents a News post.
# It extends the base functionality with:
#   - attributes: the city where the news occurred,
#   - methods: formatting end lines, specific to News posts.
class News(Post):
    post_type = 'News'
    type_id = 1
    post_prompt = '\nEnter the city: '

    def __init__(self, text, city):
        super().__init__(text)
        self._city = validators.validate_str(city, text_type='city', length=50).title()

    # Combine end line in format: "<City>, <Current date in required format>"
    def _add_end_line(self):
        return f'{self._city}, {self._cur_date.strftime("%d/%m/%Y %H.%M")}'

    # Verify if post already exists in database
    def is_stored_in_db(self, connection):
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM News WHERE text = ? AND city = ?', (self._text, self._city))
            result = True if cursor.fetchone() is not None else False
            return result

    # Write post into database.
    # The data is populated in two tables: the Posts table and the table for storing posts of required type, e.g. News
    def store_in_db(self, connection):
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO Posts (type_id, create_date) VALUES (?, ?)', (self.type_id, self._cur_date))
            cursor.execute("SELECT last_insert_rowid()")
            post_id = cursor.fetchone()[0]
            cursor.execute('INSERT INTO News (post_id, text, city) VALUES (?, ?, ?)', (post_id, self._text, self._city))
            connection.commit()
