import numpy as np

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Taking user input for a NumPy array with integers
user_input = input("Enter space-separated integers for the NumPy array: ")
numpy_array = np.fromstring(user_input, dtype=int, sep=' ')

# Taking user input for the integer to find
key_to_find = int(input("Enter the integer to find in the array: "))

# Performing linear search using the function
result = linear_search(numpy_array, key_to_find)

# Displaying the result
if result != -1:
    print(f"The integer {key_to_find} is found at index {result}.")
else:
    print(f"The integer {key_to_find} is not found in the array.")
