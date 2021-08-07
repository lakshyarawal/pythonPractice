""" Greatest Common Divisor """

""" Naive Solution: Iterating from min(a, b) to 1 t find largest common divisor """


def gcd(a, b) -> int:
    num_gcd = 1
    for i in range(min(a, b) + 1, 1, -1):
        if a % i == 0 and b % i == 0:
            return i
    return num_gcd


""" Efficient Solution: Using Euclidean Algorithm, we know gcd(a, b) = gcd (a-b, b), b is the smaller number """


def gcd_ecd(a, b) -> int:
    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a
    return a


def gcd_ecd_eff(a, b) -> int:
    if b == 0:
        return a
    else:
        return gcd_ecd_eff(b, a % b)


def main():
    val1 = int(input("Enter your value: "))
    val2 = int(input("Enter another value: "))
    ans = gcd(val1, val2)
    ans_2 = gcd_ecd(val1, val2)
    ans_3 = gcd_ecd_eff(val1, val2)
    print(ans)
    print(ans_2)
    print(ans_3)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
