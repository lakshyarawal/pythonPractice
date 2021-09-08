""" Palindrome Check : To see if a given string is palindrome or not """


"""Implementation"""


def subsequence_check(str_in, str_in2) -> bool:
    index_search = 0
    for i in range(len(str_in)):
        if str_in[i] == str_in2[index_search]:
            index_search += 1
    return index_search == len(str_in2)


def main():
    str_input = "geeksforgeeks"
    str_input2 = "grges"
    print(subsequence_check(str_input, str_input2))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
