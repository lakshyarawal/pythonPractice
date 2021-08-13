""" Two Odd Occurring: Given an array of Integers find two numbers that occurs odd number of times
    Alternate:  """

""" Naive Solution: Using nested loop find occurrence of each element and then check if it is odd"""
""" Another Solution: Do XOR of All Numbers. You would be left with XOR of two odd occurring elements.
    Since XOR is set where bits are different for both numbers, divide the array into 2 parts:
    numbers with that bit set and numbers with that bit not set"""


def two_odd_occur(a) -> list:
    two_odd = []
    result = 0
    for i in range(len(a)):
        result = result ^ a[i]
    x = result & ~(result - 1)
    """This x is the number we can use to differentiate in the two groups as this will have only that bit set which 
       is set """
    print(x)
    res_g1 = 0
    res_g2 = 0
    for i in a:
        if i & x == 0:
            res_g1 = res_g1 ^ i
        else:
            res_g2 = res_g2 ^ i
    two_odd.append(res_g1)
    two_odd.append(res_g2)
    return two_odd


""" Using XOR operator: XOR of a number with itself is 0. 
    So If you XOR of all numbers, all even occurring numbers will cancel out each other. """


def two_odd_occur_eff(a) -> list:
    two_odd_eff = []
    return two_odd_eff


def main():
    lst = []

    # number of elements as input
    n = int(input("Enter number of elements : "))

    # iterating till the range
    for i in range(0, n):
        ele = int(input())
        lst.append(ele)  # adding the element
    ans = two_odd_occur(lst)
    ans_eff = two_odd_occur_eff(lst)
    print(ans, ans_eff)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
