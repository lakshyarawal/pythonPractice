""" Lowest Common Multiple """
from gcd import gcd_ecd_eff
""" Naive Solution:  """


def lcm(a, b) -> int:
    max_num = max(a, b)
    num_lcm = max_num
    while max_num <= a*b:
        if max_num % a == 0 and max_num % b == 0:
            return max_num
        max_num = max_num + num_lcm
    return num_lcm


""" Efficient Solution: As per the euclidean algorithm, a*b = gcd(a,b) * lcm(a,b)  """


def lcm_eff(a, b) -> int:
    max_eff = int(a*b / gcd_ecd_eff(a, b))
    return max_eff


def main():
    val1 = int(input("Enter your value: "))
    val2 = int(input("Enter another value: "))
    ans = lcm(val1, val2)
    ans2 = lcm_eff(val1, val2)
    print(ans)
    print(ans2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
