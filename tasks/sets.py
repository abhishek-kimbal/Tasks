class MySet:
    def __init__(self):
        self.my_set = set()

    def add_element(self, element):
        self.my_set.add(element)
        print(f"Element '{element}' added to the set.")

    def remove_element(self, element):
        if element in self.my_set:
            self.my_set.remove(element)
            print(f"Element '{element}' removed from the set.")
        else:
            print(f"Element '{element}' not found in the set.")

    def display_set(self):
        if not self.my_set:
            print("The set is empty.")
        else:
            print("Set:", self.my_set)

    def union_sets(self, other_set):
        result_set = self.my_set.union(other_set)
        print("Union of sets:", result_set)
        return result_set

    def intersection_sets(self, other_set):
        result_set = self.my_set.intersection(other_set)
        print("Intersection of sets:", result_set)
        return result_set

    def difference_sets(self, other_set):
        result_set = self.my_set.difference(other_set)
        print("Difference of sets:", result_set)
        return result_set

my_set = MySet()

my_set.add_element(1)
my_set.add_element(2)
my_set.add_element(3)

my_set.display_set()

my_set.remove_element(2)

my_set.display_set()

other_set = {3, 4, 5}

union_result = my_set.union_sets(other_set)
intersection_result = my_set.intersection_sets(other_set)
difference_result = my_set.difference_sets(other_set)
