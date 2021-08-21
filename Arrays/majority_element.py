""" Majority Element: An element that occurs in the array more than n/2 times. For size 5 -> 3, 6 -> 4  """
import math
"""Solution:  """


def majority_element(a) -> int:
    n = len(a)
    for i in range(n):
        curr_count = 1
        for j in range(i+1, n):
            if a[i] == a[j]:
                curr_count += 1
        print(a[i], curr_count)
        if curr_count > n//2:
            return i
    return -1


def majority_element_eff(a) -> int:
    n = len(a)
    res = 0
    count = 1
    for i in range(1, n):
        if a[i] == a[res]:
            count += 1
        else:
            count -= 1
        if count == 0:
            res = i
            count = 1
    count = 0
    for i in range(n):
        if a[res] == a[i]:
            count += 1
    if count > n//2:
        return res
    return -1


def main():
    arr_input = [6, 8, 4, 8, 8]
    a3 = majority_element_eff(arr_input)
    print(a3)
    a2 = majority_element(arr_input)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
