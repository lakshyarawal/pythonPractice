""" Check if the number is prime """
import math
""" Naive Solution: Similar to prime numbers check if prime and divide """
""" Efficient Solution use sqrt and same logic as prime numbers"""


def prime_factors(a) -> list:
    prime_fact_list = []
    if a <= 1:
        return prime_fact_list
    while a > 1:
        if a % 2 == 0:
            prime_fact_list.append(2)
            a = a//2
            continue
        if a % 3 == 0:
            prime_fact_list.append(3)
            a = a//3
            continue
        else:
            break
    i = 5
    while i <= int(math.sqrt(a)):
        if a == 1:
            break
        if a % i == 0:
            prime_fact_list.append(i)
            a = a//i
            continue
        if a % (i+2) == 0:
            prime_fact_list.append(i+2)
            a = a//(i+2)
            continue
        else:
            i = i + 6
            continue
    if a > 3:
        prime_fact_list.append(a)
    return prime_fact_list


def main():
    val1 = int(input("Enter your value: "))
    a = prime_factors(val1)
    print(a)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
