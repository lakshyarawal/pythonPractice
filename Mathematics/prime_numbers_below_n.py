""" Sieve of Eratosthenes: All Prime Numbers below N """
import math
""" Naive Solution: Check if each number is prime and then add to list ( O(N * rootN) ) """


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


def prime_num(a) -> list:
    list_prime = []
    for i in range(2, a+1):
        if is_prime_eff(i):
            list_prime.append(i)
    return list_prime


""" Efficient Solution: Creating a boolean array to identify if the integers are prime """


def prime_num_eff(a) -> list:
    list_eff_prime = [True] * (a+1)
    list_prime_eff = []
    i = 2
    while i < a+1:
        if list_eff_prime[i]:
            list_prime_eff.append(i)
            for j in range(i*i, a+1, i):
                list_eff_prime[j] = False
        i = i+1
    return list_prime_eff


def main():
    val1 = int(input("Enter your value: "))
    a = prime_num(val1)
    b = prime_num_eff(val1)
    print(a)
    print(b)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
