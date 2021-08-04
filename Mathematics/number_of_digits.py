"""
Number of Digits in a number
"""
import math

""" Iterative Solution """


def count_digit(n):
    count = 0
    while n != 0:
        n = n//10
        count = count + 1
    return count


"""Recursive Solution"""


def count_digit_rec(n):
    if n//10 == 0:
        return 1
    else:
        return 1 + count_digit_rec(n//10)


"""Log Solution"""


def count_digit_log(n):
    return math.floor(math.log(n, 10)+1)


x = count_digit(147823)
y = count_digit_rec(147823)
z = count_digit_log(147823)
print(x)
print(y)
print(z)
