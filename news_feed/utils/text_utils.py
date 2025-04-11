import collections
import re


# Normalize case of each sentence in given text
def normalize_text_case(text):
    sentences_lst = re.split(r'([.!?]\s*|:\s*\n\s*)', text)
    normalized_lst = [x.capitalize() for x in sentences_lst]
    return ''.join(normalized_lst)


# Function to count occurrences of specified entities (words or letters) in a given text.
#   Parameters:
#   - text (str): The input text to process.
#   - entity (str): Specifies the entity type to count based on regex pattern. Can be 'word' or 'letter'. Default is 'word'.
#   - to_lower (bool): Whether to convert the text to lowercase before processing. Default is True.
#   Returns:
#   - counted_entities: Dictionary wth keys as selected entity (either words or letters) and values as count of entity occurrences.
def count_entity(text, entity='word', to_lower=True):
    if to_lower:
        text = text.lower()
    text = re.sub(r'[\d_]', r'', text)
    if entity == 'word':
        pattern = r"\b[\w'-]+\b"
    elif entity == "letter":
        pattern = r"\w"
    else:
        raise ValueError('Counter supports only "word" and "letter" options')
    entity = re.findall(pattern, text)
    counted_entities = collections.Counter(entity)
    return counted_entities


# Function to calculate statistics with the counts per letters.
#   Parameter: Dictionary with pairs of letters (in different case) and their counts.
#   Returns: List with dictionaries including next info: letter, count_all, count_uppercase, percentage. List is sorted alphabetically.
def get_stats(counted_entities):
    entity_stats = {}
    total_count = sum(list(counted_entities.values()))
    for key in counted_entities:
        if entity_stats.get(key.lower()) is None:
            count_upper = counted_entities.get(key.upper(), 0)
            count_lower = counted_entities.get(key.lower(), 0)
            count_all = count_upper + count_lower
            entity_stats[key.lower()] = {
                'letter': key.lower(),
                'count_all': count_all,
                'count_uppercase': count_upper,
                'percentage': str(round(100 * count_all / total_count, 2)) + '%'
            }
    result = list(entity_stats.values())
    return sorted(result, key=lambda x: x['letter'])
