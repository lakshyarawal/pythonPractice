""" All Divisors of a Number """
import math
""" Naive Solution:  """


def divisors(a) -> list:
    list_divisors = []
    for i in range(1, a+1):
        if a % i == 0:
            list_divisors.append(i)
    return list_divisors


""" Efficient Solution:  """


def divisors_eff(a) -> list:
    list_eff_divisors = []
    for i in range(1, int(math.sqrt(a))+1):
        if a % i == 0:
            list_eff_divisors.append(i)
    for i in range(len(list_eff_divisors)-1, -1, -1):
        if list_eff_divisors[i] != a//list_eff_divisors[i]:
            list_eff_divisors.append(a//list_eff_divisors[i])
    return list_eff_divisors


def main():
    val1 = int(input("Enter your value: "))
    a = divisors(val1)
    b = divisors_eff(val1)
    print(a)
    print(b)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
