import os.path

import pyodbc

from news_feed.configs import *
from news_feed.posts.post import Post
from news_feed.services.db_services import fetch_posts_from_db
from news_feed.services.file_services import read_file, read_json_file, read_xml_file
from news_feed.services.post_services import publish_post, publish_multiple_posts, write_stats_to_csv
from news_feed.services.prompt_services import select_option
from news_feed.utils.parsers import parse_post_list, parse_posts_from_json, parse_posts_from_xml


# The main function serves as the entry point of the program.
# It allows the user to select a post type and add posts until they choose to exit.
# It also allows user to provide posts from file.
def main():
    print("Hello! Let's start updating the news feed!")
    paths = {
        INPUT_FILE: INPUT_FILE_PATH,
        INPUT_JSON: INPUT_JSON_PATH,
        INPUT_XML: INPUT_XML_PATH,
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
                    write_stats_to_csv(paths[OUTPUT_FILE], WORDS_COUNT_PATH, LETTERS_COUNT_PATH)
                else:
                    print(f'Error has been logged to: {paths[ERROR_FILE]}.')
            elif option == DEFAULT_FILE:
                try:
                    lines = read_file(paths[INPUT_FILE])
                    raw_posts = parse_post_list(lines)
                    publish_multiple_posts(raw_posts, paths[INPUT_FILE], paths[OUTPUT_FILE], paths[ERROR_FILE],
                                           WORDS_COUNT_PATH, LETTERS_COUNT_PATH)
                except Exception as e:
                    print(e)
            elif option == DEFAULT_JSON:
                try:
                    json_posts = read_json_file(paths[INPUT_JSON]).get('posts')
                    raw_posts = parse_posts_from_json(json_posts)
                    publish_multiple_posts(raw_posts, paths[INPUT_JSON], paths[OUTPUT_FILE], paths[ERROR_FILE],
                                           WORDS_COUNT_PATH, LETTERS_COUNT_PATH)
                except Exception as e:
                    print(e)
            elif option == DEFAULT_XML:
                try:
                    posts_root = read_xml_file(paths[INPUT_XML])
                    raw_posts = parse_posts_from_xml(posts_root)
                    publish_multiple_posts(raw_posts, paths[INPUT_XML], paths[OUTPUT_FILE], paths[ERROR_FILE],
                                           WORDS_COUNT_PATH, LETTERS_COUNT_PATH)
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
