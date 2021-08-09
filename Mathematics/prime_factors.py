""" Check if the number is prime """
import math
""" Naive Solution:  """


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


""" Efficient Solution: """


def prime_factors_eff(a) -> list:
    prime_fact_eff_list = []
    return prime_fact_eff_list


def main():
    val1 = int(input("Enter your value: "))
    a = prime_factors(val1)
    b = prime_factors_eff(val1)
    print(a)
    print(b)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
