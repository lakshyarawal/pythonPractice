""" Iterative Power: Find x raised to the power y efficiently """

"""Solution: Use bitwise operators to convert power into binary. All powers can be written as the combination of 
power of 2. 3^7 = 3^4 * 3^2 * 3^1. The AND operator checks for 1 Bit, Right Shift moves Bits to check from LSB to MSB"""


def comp_power(a, b) -> int:
    power_result = 1
    while b > 0:
        if b & 1:
            power_result = power_result * a
        a = a * a
        b = b >> 1
    return power_result


def main():
    val1 = int(input("Enter your value: "))
    val2 = int(input("Enter another value: "))
    ans = comp_power(val1, val2)
    print(ans)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
