""" One Odd Occurring: Given an array of Integers find the number that occurs odd number of times
    Alternate: Given an array of n numbers in range [ 1 .. n+1 ] Every number appears once. Find the missing no. """

""" Naive Solution: Use nested loops and count occurrence of each number in one iteration O(n^2) """
""" Another Solution: use dictionary to map frequencies and check which number is present odd times """


def one_odd_occur(a) -> int:
    is_one_odd = a[0]
    mp = dict()

    # Traverse through array elements
    # and count frequencies
    for i in range(len(a)):
        if a[i] in mp.keys():
            mp[a[i]] += 1
        else:
            mp[a[i]] = 1
    for x in mp:
        if mp[x] % 2 != 0:
            is_one_odd = x
    return is_one_odd


""" Using XOR operator: XOR of a number with itself is 0. 
    So If you XOR of all numbers, all even occurring numbers will cancel out each other. """


def one_odd_occur_eff(a) -> int:
    is_one_odd_eff = 0
    for i in range(len(a)):
        is_one_odd_eff = is_one_odd_eff ^ a[i]
    return is_one_odd_eff


def main():
    lst = []

    # number of elements as input
    n = int(input("Enter number of elements : "))

    # iterating till the range
    for i in range(0, n):
        ele = int(input())
        lst.append(ele)  # adding the element
    ans = one_odd_occur(lst)
    ans_eff = one_odd_occur_eff(lst)
    print(ans, ans_eff)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
