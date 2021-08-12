""" Bitwise Operators """

""" AND Operator: 1 when both bits are 1 """


def and_operator(a, b) -> int:
    return a & b


""" OR Operator: 1 when any one of the bits is 1 """


def or_operator(a, b) -> int:
    return a | b


""" XOR Operator" 1 when both bits are different """


def xor_operator(a, b) -> int:
    return a ^ b


""" Left Shift Operator: If we assume that the leading y bits are 0, then result of x << y is equal to x * 2^y  """


def left_shift_operator(a, b) -> int:
    return a << b


""" Right Shift Operator: Totally opposite of Left Shift. x >> y is equal to floor of  x / 2^y  """


def right_shift_operator(a, b) -> int:
    return a >> b


""" Not Operator: Reverts all set bits 1 -> 0 and 0 -> 1  """


def not_operator(a) -> int:
    return ~a


def main():
    val1 = int(input("Enter your value: "))
    val2 = int(input("Enter another value: "))
    ans = and_operator(val1, val2)
    ans2 = or_operator(val1, val2)
    ans3 = xor_operator(val1, val2)
    ans4 = left_shift_operator(val1, val2)
    ans5 = right_shift_operator(val1, val2)
    ans6 = not_operator(val1)
    print(ans)
    print(ans2)
    print(ans3)
    print(ans4)
    print(ans5)
    print(ans6)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()