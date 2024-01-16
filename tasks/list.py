class MyList:
    def __init__(self):
        self.my_list = []

    def add_element(self, element):
        self.my_list.append(element)
        print(f"Element '{element}' added to the list.")

    def remove_element(self, element):
        if element in self.my_list:
            self.my_list.remove(element)
            print(f"Element '{element}' removed from the list.")
        else:
            print(f"Element '{element}' not found in the list.")

    def display_list(self):
        if not self.my_list:
            print("The list is empty.")
        else:
            print("List:", self.my_list)

    def get_element_at_index(self, index):
        if 0 <= index < len(self.my_list):
            return f"Element at index {index}: {self.my_list[index]}"
        else:
            return f"Invalid index {index}. Index out of range."

    def update_element_at_index(self, index, new_element):
        if 0 <= index < len(self.my_list):
            self.my_list[index] = new_element
            print(f"Element at index {index} updated to '{new_element}'.")
        else:
            print(f"Invalid index {index}. Index out of range.")

# Creating an instance of the list
my_list = MyList()

# Adding elements to the list
my_list.add_element(1)
my_list.add_element(2)
my_list.add_element(3)

# Displaying the list
my_list.display_list()

# Removing an element from the list
my_list.remove_element(2)

# Displaying the updated list
my_list.display_list()

# Getting element at a specific index
result = my_list.get_element_at_index(1)
print(result)

# Updating element at a specific index
my_list.update_element_at_index(0, 10)

# Displaying the final list
my_list.display_list()
