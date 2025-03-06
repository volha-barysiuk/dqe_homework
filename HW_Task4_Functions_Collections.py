from copy import deepcopy
import random
from string import ascii_lowercase as letters   # Import letters from 'a' to 'z' for possible keys


'''
Define the function that creates a list of 'n' number of dictionaries, where:
- Keys represent random letters.
- Values represent a random number in a specified range from 'a' to 'b'
Example outcome: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
Function accepts following parameters: n - number of dicts (set to 2 by default), a and b - min and max range values (set to 0 and 100 by default)
'''
def get_lst_with_dicts(n=2, a=0, b=100):
    result = []                                                 # List to hold the generated dictionaries
    if n:                                                       # Execute only if number of dicts is not 0
        for _ in range(n):                                      # Loop for all the dictionaries
            keys_num = random.randint(1, len(letters))      # Generate a random number of keys to have in the dictionary
            sample_dict = {keys: random.randint(a, b) for keys in random.sample(letters, keys_num)}  # Create a dictionary with random key-value pairs
            result.append(sample_dict)                          # Add sample dictionary to the list
    return result                                               # Return the resulting list with dictionaries

'''
Define the function that transforms incoming list with dictionaries to a combined dictionary with following items:
- Keys equal to the keys from the initial dictionary.
- Values equal to the list containing tuples with value and index of the initial dictionary.
Example outcome: {'a': [(5, 0), (3, 1)], 'b': [(7, 0)]}
Function accepts following parameter: List with dictionaries
'''
def combine_dicts(list_with_dicts):
    if type(list_with_dicts) is not list:                                       # Ensure the input is a list
        raise TypeError('Parameter accepts only lists')                         # Raise TypeError if not
    list_deepcopy = deepcopy(list_with_dicts)                                   # Make a deepcopy to avoid modifying original list
    result = {}                                                                 # Empty dictionary to store results of the function
    if list_deepcopy:                                                           # Execute only if passed dictionary is not empty
        for i, dct in enumerate(list_deepcopy, start=1):                        # Enumerate over the list of dictionaries
            if type(dct) is not dict:                                           # Ensure each element is a dictionary
                raise TypeError('List accepts only dictionaries as elements')   # Raise TypeError if not
            for key, value in dct.items():                                      # Loop over the key-value pairs in each dictionary
               result.setdefault(key, []).append((value, i))                    # Append a tuple with value and index to the result dictionary
    return result                                                               # Return the resulting dictionary

'''
Define the function that creates a dictionary with final results:
- If a key exists in multiple dictionaries, take the max value and rename the key to include the number of the dictionary containing the max value.
- If a key exists only in one dictionary, take the key and value as is.
Example outcome: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
Function accepts following parameter: Dictionary with values as lists of tuples
'''
def get_dict_with_max_values(combined_dict):
    if type(combined_dict) is not dict:                                 # Ensure the input is a dictionary
        raise TypeError('Parameter accepts only dictionaries')          # Raise TypeError if not
    dict_deepcopy = deepcopy(combined_dict)                             # Make a deepcopy to avoid modifying the original dictionary
    result_dict = {}                                                    # Create empty dictionary to store final results
    if dict_deepcopy:                                                   # Execute only if passed dictionary is not empty
        for key, value in dict_deepcopy.items():                        # Loop over each key-value pair in the dictionary
            if type(value) is not list:                                 # Ensure the value is a list of tuples
                raise TypeError('Dictionary accepts only list values')  # Raise TypeError if not
            if value:
                if len(value) == 1:                                     # If the key is only present in one dictionary
                    result_dict[key] = value[0][0]                      # Simply take the value
                else:                                                   # If the key appears in multiple dictionaries
                    max_value, index = max(value)                       # Get the max value and the index of the dictionary containing it
                    result_dict[f'{key}_{index}'] = max_value           # Rename the key with the dictionary index and store the max value
    return result_dict                                                  # Return the final dictionary with max values

'''
Define the function that executes the hometask with following steps:
- prompt the user to set the initial parameters,
- generate an initial list of dictionaries based on the entered parameters
- transform this list into a final dictionary containing the max values.
'''
def execute_hometask():
    print("Hello! Let's start hometask execution.")
    n = int(input('Enter a number of dictionaries to create (integer >= 0): ')) # Prompt user for number of dictionaries to create
    print('Enter the range of random values to fill in the dictionary.')
    a = int(input('Min value (integer): '))                                     # Prompt user for min value for random numbers
    b = int(input('Max value (integer): '))                                     # Prompt user for max value for random numbers
    if n < 0 or a > b:                                                          # Check for valid input
        raise ValueError
    initial_lst = get_lst_with_dicts(n, a, b)                                   # Call the function to generate initial list with 'n' dicts and values in range [a-b]
    print(initial_lst)                                                          # Print the initial list with dictionaries
    temp_dict = combine_dicts(initial_lst)                                      # Call the function to get the temporary dictionary with combined results
    result_dict = get_dict_with_max_values(temp_dict)                           # Call the function to get the final dictionary with max values
    print(result_dict)                                                          # Print the final result dictionary

# Define the main function to start the program, which handles exceptions and allows the user to either restart or stop the program.
def main(msg=None):
    while True:                                                             # Start a loop to process the user input
        try:
            execute_hometask()                                              # Execute the function to create the dictionary with final results
        except ValueError:                                                  # Handle ValueError if input is incorrect
            print(f'Error: Incorrect value entered.')
        except TypeError as e:                                              # Handle TypeError for incorrect input types
            print(f'Error: {e}')
        except Exception as e:                                              # Handle any other exceptions
            print(f'Error: Unexpected error happened, see details: {e}')    # Print unexpected error message
        answer = input('Do you want to try again? (Y/N): ')                 # Prompt user to try again
        if answer.upper() == 'Y':                                           # Continue the loop if user wants to try again
            continue
        else:
            print('Have a nice day! See you later!')                        # Exit message if user does not want to try again
            break                                                           # Break the loop and end the program

main()                                                                      # Call the main function to start the program