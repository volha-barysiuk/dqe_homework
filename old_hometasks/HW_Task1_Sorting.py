import random  # Import the random module to generate random numbers


# Create the list of random numbers
list_random = []                                        # Initialize an empty list to store random integers
n = 100                                                 # Set the size of the list to 100
for _ in range(n):                                      # Populate list_random with n random integers between 0 and 1000
    list_random.append(random.randint(0, 1000))   # Append each randomly generated number to the list

# Sort the list
for i in range(n):                      # Outer loop for each element in the list
    min_value = list_random[0]          # Assume the first element is the minimum value in the unsorted part of the list
    for j in range(1, n - i):           # Loop over the unsorted part of the list, each iteration excluding one more element from the end
        if list_random[j] < min_value:  # If a smaller value is found
            min_value = list_random[j]  # Update the min_value to the smaller value
    list_random.remove(min_value)       # Remove the min_value from list_random
    list_random.append(min_value)       # Append the found min_value to the end of list_random

# Calculate the average of even and odd numbers from the list
even_qty = 0                            # Initialize vars to store quantities and sums: Counter for even numbers
odd_qty = 0                             # Counter for odd numbers
even_sum = 0                            # Sum of even numbers
odd_sum = 0                             # Sum of odd numbers

for num in list_random:                 # Loop through each number in the list
    if num % 2:                         # Check if the number is odd (num % 2 returns 1 for odd numbers)
        odd_sum += num                  # Add the odd number to the odd_sum
        odd_qty += 1                    # Increment the counter for odd numbers
    else:
        even_sum += num                 # Add the even number to the even_sum
        even_qty += 1                   # Increment the counter for even numbers

avg_odd = round(odd_sum / odd_qty, 2) if odd_qty > 0 else 0         # Calculate the average of odd numbers
                                                                    # Round to 2 decimals. Avoid division by zero
avg_even = round(even_sum / even_qty, 2) if even_qty > 0 else 0     # Calculate the average of even numbers
                                                                    # Round to 2 decimals. Avoid division by zero

# Print the results
print(f'Sorted list of {n} random integers from 0 to 1000: {list_random}')
print(f'Average of even numbers is {avg_even}')
print(f'Average of odd numbers is {avg_odd}')