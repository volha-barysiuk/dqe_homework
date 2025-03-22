from .post import Post
from ..utils import validators


# PrivateAd class inherits from the Post class and represents a Private Ad post.
# It extends the base functionality with:
#   - Attributes: the date when the ad expires,
#   - Methods: date validation; formatting end lines, specific to Private Ad posts.
class PrivateAd(Post):
    post_type = 'Private Ad'
    post_prompt = '\nEnter expiration date (dd/mm/yyyy): '

    def __init__(self, text, exp_date):
        super().__init__(text)
        self._exp_date = validators.validate_future_date(self._cur_date, validators.validate_date(exp_date))

    # Combine end line in format: "Actual until: <expiry_date_in_required_format>, <days_number> days left"
    def _add_end_line(self):
        exp_date = self._exp_date.strftime('%d/%m/%Y')
        days_diff = (self._exp_date - self._cur_date).days
        return f'Actual until: {exp_date}, {days_diff} day{'' if days_diff == 1 else 's'} left'