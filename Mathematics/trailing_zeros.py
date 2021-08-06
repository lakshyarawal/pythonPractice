""" How many trailing zeros are there in the numbers factorial """
from factorial import factorial

""" Naive Method: Find the Factorial and then divide by 10 and check the remainder """


def trailing_zeros(n) -> int:
    zeros = 0
    fact = factorial(n)
    print(fact)
    while fact % 10 == 0:
        zeros += 1
        fact = fact // 10
    return zeros


""" Revised Method: Find the number of 5s in the number factorial to find trailing zeros as it comes from 2x5 """


def trailing_zeros_rev(n) -> int:
    rev_zero = 0
    k = 5
    while k <= n:
        rev_zero = rev_zero + n//k
        k = k * 5
    return rev_zero


# Defining main function
def main():
    val = int(input("Enter your value: "))
    ans = trailing_zeros(val)
    ans_rev = trailing_zeros_rev(val)
    print(ans_rev)
    print(ans)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
