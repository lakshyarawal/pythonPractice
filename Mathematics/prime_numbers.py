""" Check if the number is prime """
import math
""" Naive Solution:  """


def is_prime(a) -> int:
    is_prime_num = True
    for i in range(2, a):
        if a % i == 0:
            is_prime_num = False
            return is_prime_num
    return is_prime_num


""" Efficient Solution: replace a by int(math.sqrt(a)) as divisors occur in pairs only """
""" More efficient solution: Check basic divisions like 2 and 3 earlier """


def is_prime_eff(a) -> int:
    is_prime_eff_num = True
    if a == 2 or a == 3:
        return is_prime_eff_num
    if a % 2 == 0 or a % 3 == 0:
        is_prime_eff_num = False
        return is_prime_eff_num
    for i in range(5, int(math.sqrt(a)), 6):
        if a % i == 0 or a % (i+2) == 0:
            is_prime_eff_num = False
            return is_prime_eff_num
    return is_prime_eff_num


def main():
    val1 = int(input("Enter your value: "))
    if is_prime(val1):
        print("It is a prime number")
    else:
        print("It is not a prime number")
    if is_prime_eff(val1):
        print("It is a prime number")
    else:
        print("It is not a prime number")


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
