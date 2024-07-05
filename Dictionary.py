from RBTrees import RBTrees


class Dictionary:
    def __init__(self):
        self.tree = RBTrees()
        self.initialize()

    def initialize(self):
        while 1:

            print("What do you want to do ?")
            print("1 : Load Dictionary")
            print("2 : Insert a word")
            print("3 : Look up a word")
            print("4 : exit")
            case_value = int(input("Enter a number 1->4\n"))
            if case_value == 1:
                self._load_dictionary()
            elif case_value == 2:
                word = input("write a word you want to insert\n")
                self._insert_word(word)
            elif case_value == 3:
                word = input("write a word you want to look up\n")
                self._lookup_word(word)
            elif case_value == 4:
                return 0
            else:
                print("Invalid case")

    def _load_dictionary(self):
        try:
            with open("dictionary.txt", "r") as file:
                for line in file:
                    word = line.strip()  # Remove leading/trailing whitespace
                    self.tree.insert(word)  # Insert each word into the Red-Black Tree
            print("Dictionary loaded successfully.")
        except FileNotFoundError:
            print("Error: File 'dictionary.txt' not found.")

    def _insert_word(self, word):
        if self.tree.search(word):
            print("Error, Word already in dictionary!!")
        else:
            self.tree.insert(word)
            self.dictionary_file = open("dictionary.txt", "a")
            self.dictionary_file.write(word + "\n")
            print(f"Word '{word}' inserted into the dictionary.")
            print("tree height is : ", self.tree.tree_height())
            print("Black tree height is : ", self.tree.black_height())
            print("number of elements in tree is : ", self.tree.tree_size())

    def _lookup_word(self, word):
        if self.tree.search(word):
            print("Yes, it's found")
        else:
            print("No, it's not found")
