""" Is the Given Number a palindrome or not """
val = int(input("Enter your value: "))


def is_palindrome(n):
    rev = 0
    temp = n
    while temp >= 1:
        ld = temp % 10
        rev = rev * 10 + ld
        temp = temp//10
    return rev == n


if is_palindrome(val):
    print("Its a palindrome")
else:
    print("Its not a palindrome")