import re


debug_text = '''homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces.  I got 87.'''


# Define the function to create extra sentence combined of the last words of specified text
def get_last_words_sentence(text):
    last_words_lst = re.findall(r'(\b\w+\b)[.?!]+', text)               # Collect the last word of each sentence
    return ' '.join(last_words_lst)                                             # Join the last words with spaces to form a new sentence. Return the sentence

# Define the function to put specified sentence after specified text-part from the initial text
def add_extra_sentence(text, text_part, extra_sentence):
    return re.sub(rf'({text_part}[.!?])',                                              # Find the specific text-part where extra sentence should be added
                           rf'\1 {extra_sentence}.', text, count=1, flags=re.I)     # Add extra sentence after the first occurance of matched text

# Define the function to correct the misspelled word "iz" to "is" in specified text
def correct_misspelled_iz(text):
    return re.sub(r'(\s)(\biz\b)|(\biz\b)(\s)',                         # Find and replace case-insensitive "iz" with "is". Keep the spaces around
                               r'\1is\4', text, flags=re.I)                 # Return corrected text

# Define the function to normalize the text by adjusting the case of each sentence
def normalize_text_case(text):
    sentences_lst = re.split(r'([.!?]\s*|:\s*\n\s*)', text)             # Split the text into sentences
    normalized_lst = [x.capitalize() for x in sentences_lst]                    # Capitalize the first letter of each sentence
    return ''.join(normalized_lst)                                              # Join the sentences. Return case-normalized text

# Define the function to count all whitespaces in the initial text
def count_whitespaces(text):
    spaces_lst = re.findall(r'\s', text)
    return len(spaces_lst)

# Define the main function to execute the hometask  and print the results
def execute_hometask():
    print("Hello! Let's start hometask execution.")
    print("Enter the initial text you want to refine. Print 'END' and press 'Enter' when done:")
    lines = []
    while True:
        line = input()
        if line == 'END':
            break
        lines.append(line)
    initial_text = '\n'.join(lines)
    text_part = input("Enter the sentence after which to insert the extra sentence (at least few last words to accurately locate the sentence, avoid punctuation marks):\n")
    extra_sentence = get_last_words_sentence(initial_text)
    extended_text = add_extra_sentence(initial_text, text_part, extra_sentence)
    corrected_text = correct_misspelled_iz(extended_text)
    normalized_text = normalize_text_case(corrected_text)
    whitespaces_num = count_whitespaces(initial_text)
    print(f"Final text normalized case-wise, with extra sentence:\n{normalized_text}\n\n")
    print(f"The number of whitespaces in initial text (before modifications): {whitespaces_num}")

execute_hometask()