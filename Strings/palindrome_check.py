""" Palindrome Check : To see if a given string is palindrome or not """


"""Implementation"""


def palindrome_check(str_in) -> bool:
    for i in range(len(str_in)//2):
        if str_in[i] != str_in[-(i+1)]:
            return False
    return True


def main():
    str_input = "ABCDCBA"
    print(palindrome_check(str_input))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
