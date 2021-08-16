""" Generate Subsets: Given a string generate all subsets using recursion """

"""Solution: Recursively make calls for string by including and not including character at index I, this will create 
    all combinations in the form of a tree """


def generate_subsets(a, final_str, index_int):
    if index_int == len(a):
        print(final_str)
        return
    generate_subsets(a, final_str, index_int + 1)
    generate_subsets(a, final_str + a[index_int], index_int+1)


def main():
    val1 = input("Enter your string: ")
    curr = ""
    int_val = 0
    generate_subsets(val1, curr, int_val)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
