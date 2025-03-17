import re
from datetime import datetime
from random import sample, choice


class Post:
    def __init__(self, post_type, text):
        self._post_type = post_type
        self._text = self.validate_text_length(text)
        self._cur_date = datetime.now()

    @staticmethod
    def validate_text_length(text, length=100):
        if len(text) > length:
            raise ValueError(f'Text length should not exceed {length} characters.')
        return text

    @staticmethod
    def normalize_text_case(text):
        sentences_lst = re.split(r'([.!?]\s*|:\s*\n\s*)', text)
        normalized_lst = [x.capitalize() for x in sentences_lst]
        return ''.join(normalized_lst)

    def _format_post(self, end_line=None):
        title = self._post_type + '_' * 10
        result = [title, self.normalize_text_case(self._text)]
        if end_line is not None:
            result.append(end_line)
        return '\n'.join(result)

    def publish(self):
        with open('News Feed.txt', 'a') as file:
            file.write(self._format_post() + '\n\n')


class News(Post):
    def __init__(self, text, city):
        super().__init__('News', text)
        self._city = self.validate_text_length(city, length=50).title()

    def _format_post(self, end_line=None):
        end_line = f'{self._city}, {self._cur_date.strftime('%d/%m/%Y %H.%M')}'
        return super()._format_post(end_line)


class PrivateAd(Post):
    def __init__(self, text, exp_date):
        super().__init__('Private Ad', text)
        self._exp_date = self.validate_date(exp_date)

    def validate_date(self, exp_date):
        exp_date = datetime.strptime(exp_date, '%d/%m/%Y')
        if exp_date <= self._cur_date:
            raise ValueError('Past dates are not allowed.')
        return exp_date

    def _format_post(self, end_line=None):
        days_left = self._exp_date - self._cur_date
        exp_date = self._exp_date.strftime('%d/%m/%Y')
        end_line = f'Actual until: {exp_date}, {days_left.days} days left'
        return super()._format_post(end_line)


class Rumor(Post):
    shock_phrase = ["You won't believe this!",
                    "This will shock you!",
                    "Guess what just happened?!",
                    "Hold on to your seat!",
                    "You won't see this coming!",
                    "This is jaw-dropping!",
                    "Prepare to be amazed!"]
    score = ['one', 'two', 'three', 'four', 'five']

    def __init__(self, text, celebrity):
        text = choice(self.shock_phrase) + '\n' + text
        super().__init__('Rumor', text)
        self._celebrity = self.validate_text_length(celebrity, length=50).title()

    def _format_post(self, end_line=None):
        end_line = f'Celebrity involved: {self._celebrity}\nRumor clickbait score: {choice(self.score)} of ten'
        return super()._format_post(end_line)

def add_post(post_type):
    print(f'Enter the text of your {post_type.lower()}: ')
    text = Post.validate_text_length(input())
    if post_type == 'News':
        city = input('Enter the city where the news happened: ')
        post = News(text, city)
    elif post_type == 'Private Ad':
        exp_date = input('Enter expiration date of your private ad (format: dd/mm/yyyy): ')
        post = PrivateAd(text, exp_date)
    elif post_type == 'Rumor':
        celebrity = input('Enter the celebrity about whom your rumor is: ')
        post = Rumor(text, celebrity)
    else:
        raise ValueError("You've entered incorrect post type option.")
    post.publish()


def main():
    post_types = ['News', 'Private Ad', 'Rumor']
    print("Hello, let's update the news feed!\n")
    while True:
        print("Please select the publication type you'd like to add.")
        for i, post_type in enumerate(post_types, 1):
            print(f'{i} - {post_type}')
        print('0 - Exit the program\n')
        selected_option = input('Select option: ')
        if not selected_option.isdigit() or int(selected_option) not in range(len(post_types) + 1):
            print('Incorrect post type option. Select digit from the suggested list.\n')
        elif int(selected_option):
            post_type = post_types[int(selected_option) - 1]
            try:
                add_post(post_type)
            except Exception as error_message:
                print(f'Oops! Error occured: {error_message}')
        else:
            break
        answer = input('Do you want to add new post? (Y/N): ').upper()
        if answer == 'Y':
            continue
        else:
            break
    print('Have a nice day! See you later!')

if __name__ == '__main__':
    main()
