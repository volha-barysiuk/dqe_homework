from random import choice

from .post import Post
from ..utils import validators


# Rumor class inherits from the Post class and represents a Rumor post.
# It extends the base functionality with:
#   - Attributes: celebrity the rumor is about.
#   - Methods: formatting end lines specific to Rumor posts.
class Rumor(Post):
    post_type = 'Rumor'
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
