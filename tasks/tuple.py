class MyTuple:
    def __init__(self):
        self.my_tuple = ()

    def add_element(self, element):
        self.my_tuple += (element,)
        print(f"Element '{element}' added to the tuple.")

    def display_tuple(self):
        if not self.my_tuple:
            print("The tuple is empty.")
        else:
            print("Tuple:", self.my_tuple)

    def get_element_at_index(self, index):
        if 0 <= index < len(self.my_tuple):
            return f"Element at index {index}: {self.my_tuple[index]}"
        else:
            return f"Invalid index {index}. Index out of range."

# Creating an instance of the tuple
my_tuple = MyTuple()

# Adding elements to the tuple
my_tuple.add_element(1)
my_tuple.add_element(2)
my_tuple.add_element(3)

# Displaying the tuple
my_tuple.display_tuple()

# Getting element at a specific index
result = my_tuple.get_element_at_index(1)
print(result)
