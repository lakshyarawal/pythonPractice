""" Palindrome Check: Given a string find if it is a palindrome using recursion """

"""Solution: Recursively make the string shorter until length is two or one, if two compare both and return value """


def palindrome_check(a) -> bool:
    if len(a) == 1 or len(a) == 0:
        return True
    return a[0] == a[-1] and palindrome_check(a[1:-1])


def main():
    val1 = input("Enter your string: ")
    if palindrome_check(val1):
        print("Yes")
    else:
        print("No")


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
