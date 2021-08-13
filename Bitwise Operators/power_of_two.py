""" Power of Two: To check if the given number is a power of 2 or not  """

""" Naive Solution: Keep Dividing by 2 and check remainder. If no remainder is there it is a power of 2 
    while a != 1: if a % 2 != 0  return false a = a//2"""

""" BK Algo: Check if number of set bits is equal to 1. This can be made more efficient by checking n & (n-1) == 0 """


def power_of_two(a) -> bool:
    is_power = False
    count_bk_bits = 0
    while a > 0:
        count_bk_bits += 1
        a = a & (a - 1)
    if count_bk_bits == 1:
        is_power = True
    return is_power


def power_of_two_eff(a) -> bool:
    is_power = False
    if a == 0:
        return is_power
    if a & (a-1) == 0:
        is_power = True
    return is_power


def main():
    val1 = int(input("Enter your value: "))
    if power_of_two(val1):
        print("Yes")
    else:
        print("No")
    if power_of_two_eff(val1):
        print("Yes")
    else:
        print("No")


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
