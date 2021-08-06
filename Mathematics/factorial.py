""" Factorial of a Number """

""" Iterative Solution """


def factorial(n) -> int:
    fact = 1
    while n > 1:
        fact = n * fact
        n = n-1
    return fact


""" Recursive Solution """


def factorial_rec(n) -> int:
    if n == 1:
        return 1
    return n * factorial_rec(n-1)


# Defining main function
def main():
    val = int(input("Enter your value: "))
    ans = factorial(val)
    ans_rec = factorial_rec(val)
    print(ans)
    print(ans_rec)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
