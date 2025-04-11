from .post import Post
from ..utils import validators


# PrivateAd class inherits from the Post class and represents a Private Ad post.
# It extends the base functionality with:
#   - Attributes: the date when the ad expires,
#   - Methods: date validation; formatting end lines, specific to Private Ad posts.
class PrivateAd(Post):
    post_type = 'Private Ad'
    type_id = 2
    post_prompt = '\nEnter expiration date (dd/mm/yyyy): '

    def __init__(self, text, exp_date):
        super().__init__(text)
        self._exp_date = validators.validate_future_date(self._cur_date, validators.validate_date(exp_date))

    # Combine end line in format: "Actual until: <expiry_date_in_required_format>, <days_number> days left"
    def _add_end_line(self):
        exp_date = self._exp_date.strftime('%d/%m/%Y')
        days_diff = (self._exp_date - self._cur_date).days
        return f"Actual until: {exp_date}, {days_diff} day{'' if days_diff == 1 else 's'} left"

    # Verify if post already exists in database
    def is_stored_in_db(self, connection):
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM PrivateAd WHERE text = ? AND expiry_date = ?', (self._text, self._exp_date))
            result = True if cursor.fetchone() is not None else False
            return result

    # Write post into database.
    # The data is populated in two tables: the Posts table and the table for storing posts of required type
    def store_in_db(self, connection):
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO Posts (type_id, create_date) VALUES (?, ?)', (self.type_id, self._cur_date))
            cursor.execute("SELECT last_insert_rowid()")
            post_id = cursor.fetchone()[0]
            cursor.execute('INSERT INTO PrivateAd (post_id, text, expiry_date) VALUES (?, ?, ?)',
                           (post_id, self._text, self._exp_date))
            connection.commit()
