""" Kth bit set: Find if Kth bit is set in the binary representation of the given decimal number """

"""Solution: Three Solutions using, power , left shift and right shift operator along with and operator. 
   AND with only Kth bit set as 1 is implemented below"""


def kth_bit_set(a, b) -> bool:
    num = 1 << (b - 1)

    ## Using right shift: a >> b-1 and then & with 1 and check if it is equal to 1
    ## Using power: num = pow(2, b-1)

    if a & num == 0:
        power_result = False
    else:
        power_result = True
    return power_result


def main():
    val1 = int(input("Enter your value: "))
    val2 = int(input("Enter another value: "))
    if kth_bit_set(val1, val2):
        print("Yes")
    else:
        print("No")


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
