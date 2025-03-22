import os.path

from news_feed.configs import *
from news_feed.posts.post import Post
from news_feed.services.file_services import open_file
from news_feed.services.post_services import publish_post
from news_feed.services.prompt_services import select_option
from news_feed.utils.parsers import parse_post_list


# The main function serves as the entry point of the program.
# It allows the user to select a post type and add posts until they choose to exit.
# It also allows user to provide posts from file.
def main():
    print("Hello! Let's start updating the news feed!")
    paths = {
        INPUT_FILE: INPUT_FILE_PATH,
        OUTPUT_FILE: OUTPUT_FILE_PATH,
        ERROR_FILE: ERROR_FILE_PATH
    }
    while True:
        opt_1 = select_option(MAIN_MENU)
        if not opt_1:
            break
        while True:
            opt_2 = select_option(SUB_MENU[opt_1])
            if not opt_2:
                break
            option = SUB_MENU[opt_1][opt_2]
            if option in (NEWS, PRIVATE_AD, RUMOR):
                print(Post.post_prompt)
                text = input()
                print(CLASSES[option].post_prompt)
                end_line = input()
                result = publish_post(option, text, end_line, paths[OUTPUT_FILE], paths[ERROR_FILE], True)
                if result:
                    print(f'\nPost has been successfully published to: {paths[OUTPUT_FILE]}.')
                else:
                    print(f'Error has been logged to: {paths[ERROR_FILE]}.')
            elif option == DEFAULT_FILE:
                try:
                    lines = open_file(paths[INPUT_FILE])
                    raw_posts = parse_post_list(lines)
                    for post_type, text, end_line in raw_posts:
                        publish_post(post_type, text, end_line, paths[OUTPUT_FILE], paths[ERROR_FILE])
                    print(f'\nThe file {paths[INPUT_FILE]} has been processed.')
                    print(f'If any errors were encountered, they have been logged to: {paths[ERROR_FILE]}.')
                except Exception as e:
                    print(e)
            else:
                print(f'Current file path: {paths[option]}')
                print('Specify new file path: ')
                new_file_path = input()
                if os.path.exists(new_file_path):
                    paths[option] = new_file_path
                    print(f'File path has been successfully changed to: {paths[option]}')
                else:
                    print('Specified file path does not exist')
    print('\nHave a nice day! See you later!')

if __name__ == '__main__':
    main()