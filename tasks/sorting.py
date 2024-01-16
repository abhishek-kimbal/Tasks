import numpy as np

# Function to swap two elements
def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

# Partition function to place the pivot at its correct position
def partition(arr, low, high):
    pivot = arr[low]
    left_ptr = low + 1
    right_ptr = high

    while True:
        # Move the left pointer to find the element greater than the pivot
        while left_ptr <= right_ptr and arr[left_ptr] <= pivot:
            left_ptr += 1

        # Move the right pointer to find the element smaller than the pivot
        while left_ptr <= right_ptr and arr[right_ptr] > pivot:
            right_ptr -= 1

        # If the pointers cross each other, break the loop
        if left_ptr > right_ptr:
            break

        # Swap the elements at the left and right pointers
        arr[left_ptr], arr[right_ptr] = swap(arr[left_ptr], arr[right_ptr])

    # Move the pivot to its correct position
    arr[low], arr[right_ptr] = swap(arr[low], arr[right_ptr])
    return right_ptr

# Quicksort function
def quickSort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        quickSort(arr, low, pivot_index - 1)
        quickSort(arr, pivot_index + 1, high)

# Function to print an array
def printArray(arr):
    for item in arr:
        print(item, end=" ")
    print()

# Taking user input for a NumPy array with integers
user_input = input("Enter space-separated integers for the array to be sorted: ")
arr = np.fromstring(user_input, dtype=int, sep=' ')

# Performing quicksort
quickSort(arr, 0, len(arr) - 1)

# Displaying the sorted array
print("Sorted array:", end=" ")
printArray(arr)
