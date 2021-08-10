""" Computing Power: Find x raised to the power y efficiently """
import math

""" Naive Solution:  """


def comp_power(a, b) -> int:
    power_result = 1
    if b == 0:
        return power_result
    for i in range(b):
        power_result = power_result * a
    return power_result


""" Efficient Solution: Divide the power into smaller factors by diving into 2 and then multiply  """


def comp_power_eff(a, b) -> int:
    if b == 0:
        return 1
    temp = comp_power_eff(a, b // 2)
    temp = temp * temp
    if b % 2 == 0:
        return temp
    else:
        return temp*a


def main():
    val1 = int(input("Enter your value: "))
    val2 = int(input("Enter another value: "))
    ans = comp_power(val1, val2)
    ans2 = comp_power_eff(val1, val2)
    print(ans)
    print(ans2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
