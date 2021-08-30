""" Chocolate Distribution problem: We are given packets of different sizes where packets contain the number of
    chocolates mentioned in the element. We want to distribute these packets to M children given as input
    Rules: Every child should get exactly one packet, we have to minimize the difference between the min and max
    chocolate a child gets"""
import sys

from quick_sort import quick_sort_hoare
from lomuto_partition import lom_partition

"""Solution"""


def chocolate_distribution(arr, children) -> int:
    min_difference = sys.maxsize
    low = 0
    high = len(arr) - 1
    quick_sort_hoare(arr, low, high)
    print(arr)
    for i in range(len(arr)-children + 1):
        min_difference = min(min_difference, arr[i+children-1]-arr[i])
    return min_difference


def chocolate_distribution_eff(arr, children) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        p = lom_partition(arr, low, high)
        if p == children - 1:
            return arr[children - 1]
        if p > children - 1:
            high = p - 1
        if p < children - 1:
            low = p + 1
    return -1


def main():
    arr_input = [3, 4, 1, 9, 56, 7, 9, 12]
    print(arr_input)
    num_children = int(input("Enter number of children: "))
    a2 = chocolate_distribution(arr_input, num_children)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
