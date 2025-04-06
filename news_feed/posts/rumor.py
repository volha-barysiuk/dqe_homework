from random import choice

from .post import Post
from ..utils import validators


# Rumor class inherits from the Post class and represents a Rumor post.
# It extends the base functionality with:
#   - Attributes: celebrity the rumor is about.
#   - Methods: formatting end lines specific to Rumor posts.
class Rumor(Post):
    post_type = 'Rumor'
    type_id = 3
    post_prompt = '\nEnter the celebrity a rumor is about: '

    # List of opening phrases to make the rumor more engaging.
    shock_phrase = ["You won't believe this!",
                    "This will shock you!",
                    "Guess what just happened?!",
                    "Hold on to your seat!",
                    "You won't see this coming!",
                    "This is jaw-dropping!",
                    "Prepare to be amazed!"]
    # List of possible scores to evaluate clickbait level of the rumor at the end of the post.
    score = ['one', 'two', 'three', 'four', 'five']

    def __init__(self, text, celebrity):
        super().__init__(choice(self.shock_phrase) + '\n' + text)
        self._celebrity = validators.validate_str(celebrity, text_type='celebrity name', length=50).title()

    # Combine end line in format below and assign random score to a rumor. End line format:
    # "Celebrity involved: <celebrity>\nRumor clickbait score: <random_score> of five"
    def _add_end_line(self):
        return f'Celebrity involved: {self._celebrity}\nRumor clickbait score: {choice(self.score)} of five'

    # Verify if post already exists in database
    def is_stored_in_db(self, connection):
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM Rumor WHERE text = ? AND celebrity = ?', (self._text, self._celebrity))
            result = True if cursor.fetchone() is not None else False
            return result

    # Write post into database.
    # The data is populated in two tables: the Posts table and the table for storing posts of required type, e.g. Rumor
    def store_in_db(self, connection):
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO Posts (type_id, create_date) VALUES (?, ?)', (self.type_id, self._cur_date))
            cursor.execute("SELECT last_insert_rowid()")
            post_id = cursor.fetchone()[0]
            cursor.execute('INSERT INTO Rumor (post_id, text, celebrity) VALUES (?, ?, ?)', (post_id, self._text, self._celebrity))
            connection.commit()