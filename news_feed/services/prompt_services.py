from ..utils.validators import validate_int


# A prompt service to interact with the user based on the selected options.
# It validates the user's input, allows navigation between main and sub-menus, and exits the program if chosen.
def select_option(option_list):
    while True:
        print("\nPlease select the option:")
        for i, option in enumerate(option_list[1:], start=1):
            print(f'{i} - {option}')
        print(f'0 - {option_list[0]}\n')
        num = input('Your choice: ')
        try:
            choice = validate_int(num, 0, len(option_list) - 1)
            return choice
        except Exception as e:
            print(e)
