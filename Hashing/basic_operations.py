
""" Basic Operations using dictionaries: Search, Insert and Delete """


def insert_element(dict_input):
    dict_input[5] = "New Element"


def deleting_element(dict_input):
    del dict_input[3]


def searching_element(dict_input):
    print(dict_input[2])


def main():
    dict_table = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
    print("Dictionary with the use of Integer Keys: ")
    print(dict_table)
    print("Adding an Element: ")
    insert_element(dict_table)
    print(dict_table)
    print("Deleting an Element: ")
    deleting_element(dict_table)
    print(dict_table)
    print("Searching an Element 2: ")
    searching_element(dict_table)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
