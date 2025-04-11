from datetime import datetime


# Validate string for correctness: it should be of string type and of acceptable length.
def validate_str(text, text_type='text', length=500):
    if type(text) is not str:
        raise TypeError(f'The {text_type.lower()} should be a string')
    if not len(text):
        raise ValueError(f'The {text_type.lower()} is empty')
    if len(text) > length:
        raise ValueError(f'The {text_type.lower()} length should not exceed {length} characters')
    return text


# Validate string and parse it to a datetime object
def validate_date(date):
    if type(date) is not str:
        raise TypeError(f'The date should be a string')
    try:
        valid_date = datetime.strptime(date, '%d/%m/%Y')
        return valid_date
    except:
        raise ValueError(f'The date should be in format "dd/mm/yyyy"')


# Compare two dates and ensure one of them is later than the other one
def validate_future_date(date, future_date):
    if future_date < date:
        raise ValueError('Past dates are not allowed.')
    return future_date


# Validate given console option selected by user,
# Raise error if it's not integer and if it's not in the range of possible choice options.
def validate_int(num, start=1, end=5):
    if not num.isdigit() or int(num) not in range(start, end + 1):
        raise ValueError('Incorrect option. Select digit from the suggested list.')
    return int(num)
