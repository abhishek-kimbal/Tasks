class MyDictionary:
    def __init__(self):
        self.dictionary = {}

    def add_word(self, word, definition):
        self.dictionary[word] = definition
        print(f"Word '{word}' added to the dictionary.")

    def search_word(self, word):
        definition = self.dictionary.get(word)
        if definition:
            return f"Definition of '{word}': {definition}"
        else:
            return f"Word '{word}' not found in the dictionary."

    def display_all_words(self):
        if not self.dictionary:
            print("The dictionary is empty.")
        else:
            print("Dictionary:")
            for word, definition in self.dictionary.items():
                print(f"{word}: {definition}")

    def remove_word(self, word):
        if word in self.dictionary:
            del self.dictionary[word]
            print(f"Word '{word}' removed from the dictionary.")
        else:
            print(f"Word '{word}' not found in the dictionary.")

    def update_word(self, word, new_definition):
        if word in self.dictionary:
            self.dictionary[word] = new_definition
            print(f"Definition of '{word}' updated in the dictionary.")
        else:
            print(f"Word '{word}' not found in the dictionary.")

# Creating an instance of the dictionary
my_dict = MyDictionary()

while True:
    print("\nDictionary Program Menu:")
    print("1. Add Word")
    print("2. Search Word")
    print("3. Display All Words")
    print("4. Remove Word")
    print("5. Update Word Definition")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        word = input("Enter the word: ")
        definition = input("Enter the definition: ")
        my_dict.add_word(word, definition)

    elif choice == '2':
        word = input("Enter the word to search: ")
        result = my_dict.search_word(word)
        print(result)

    elif choice == '3':
        my_dict.display_all_words()

    elif choice == '4':
        word = input("Enter the word to remove: ")
        my_dict.remove_word(word)

    elif choice == '5':
        word = input("Enter the word to update: ")
        new_definition = input("Enter the new definition: ")
        my_dict.update_word(word, new_definition)

    elif choice == '6':
        print("Exiting the dictionary program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
