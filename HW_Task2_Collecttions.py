import random
from string import ascii_lowercase as letters   # Import letters from 'a' to 'z' for possible keys


'''
Create a list of random number of dicts (from 2 to 10), where
- keys represent random letters,
- values represent a random number (from 0 to 100),
Example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
'''
dicts_num = random.randint(2, 10)                                                               # Randomly set the number of dictionaries to be created
list_with_dicts = []                                                                                # List to hold the generated dictionaries
for _ in range(dicts_num):                                                                          # Loop for all the dictionaries
    keys_num = random.randint(1, len(letters))                                                      # Random number of keys to have in the dictionary
    sample_dict = {keys: random.randint(0, 50) for keys in random.sample(letters, keys_num)}    # Generate sample dictionary with random key-value pairs
    list_with_dicts.append(sample_dict)                                                             # Add sample dictionary to the list

'''
Create a temporary dictionary to store following items:
 - keys equal to the keys from initial dictionary
 - values equal to the list containing tuples with value and index of initial dictionary
Example: {'a': [(5, 0), (3, 1)], 'b': [(7, 0)]}
'''
temp_dict = {}
for i in range(dicts_num):                                  # Loop over each dictionary in the list
    for key, value in list_with_dicts[i].items():           # Loop over each item in the current dictionary
       temp_dict.setdefault(key, []).append((value, i))     # Append the items into temporary dictionary

'''
Create the dictionary with the final results:
- if key exists in multiple dict: take max value, and rename the key to include the number of dict containing max value
- if key exists only in one dict: take the key and value as is
Example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
'''
result_dict = {}                                            # Final dictionary to store the results
for key, value in temp_dict.items():                        # Loop over each item in the temporary dictionary
    if len(value) == 1:                                     # If the key is only present in one dictionary
        result_dict[key] = value[0][0]                      # Simply take the value
    else:                                                   # If the key appears in multiple dictionaries
        max_value, index = max(value)                       # Get the max value and the index of the dictionary containing it
        result_dict[f'{key}_{index + 1}'] = max_value       # Rename the key with the dictionary number (index + 1) and store the max value

# Print the final result dictionary
print(result_dict)