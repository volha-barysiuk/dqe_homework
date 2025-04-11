import re


initial_text = '''homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces.  I got 87.
'''

# Add extra sentence combined of the last words
last_words_lst = re.findall(r'(\b\w+\b)[.?!]', initial_text)            # Match words followed by sentence-ending punctuation (.?!). Collect the last word of each sentence
new_sentence = ' '.join(last_words_lst)                                 # Join the list of last words with spaces to form a new sentence
extended_text = re.sub(r'(add it to the end of this paragraph\.)',      # Find the specific sentence where the new sentence should be added
                       rf'\1 {new_sentence}.', initial_text, flags=re.I)        # Replace the matched sentence with itself (\1) plus the new sentence, separated with space and ended with dot (.)

# Correct the misspelled word "iz" to "is"
iz_corrected_text = re.sub(r'(\s)(\biz\b)|(\biz\b)(\s)', r'\1is\4', extended_text, flags=re.I)  # Find and replace case-insensitive "iz" with "is". Keep the spaces around
                                                                                                        # Match pattern: 'is' should be either preceded OR followed by a space

# Normalize the text by adjusting the case of each sentence
sentences_lst = re.split(r'([.!?]\s*|:\s*\n\s*)', iz_corrected_text)  # Split the text into sentences, using punctuation marks (.?!) followed by optional whitespace,
                                                                    # or a colon (:) followed by a newline.
normalized_lst = [x.capitalize() for x in sentences_lst]            # Capitalize the first letter of each sentence
case_normalized_text = ''.join(normalized_lst)                      # Join the sentences into a resulting text with proper case

# Count all whitespace characters in the initial text
spaces_lst = re.findall(r'\s', initial_text)

# Print the results
print(f'The number of whitespaces in initial text (before modifications): {len(spaces_lst)}\n')
print(f'Text normalized case-wise, with extra sentence:\n{case_normalized_text}')