""" Sum of Digits: Given a number ABC find the sum of it's digits, Sum = A + B + C """

"""Solution: Recursively mod the number by 10 and keep adding """


def sum_of_digits(a) -> int:
    if a <= 9:
        return a
    return a % 10 + sum_of_digits(a//10)


"""Iterative Solution: While (a >0):
    res = res + a % 10
    a = a//10"""


def main():
    val1 = int(input("Enter a number: "))
    a = sum_of_digits(val1)
    print(a)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
