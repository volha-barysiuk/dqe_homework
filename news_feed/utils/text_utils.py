import re

# Normalize case of each sentence in given text
def normalize_text_case(text):
    sentences_lst = re.split(r'([.!?]\s*|:\s*\n\s*)', text)
    normalized_lst = [x.capitalize() for x in sentences_lst]
    return ''.join(normalized_lst)