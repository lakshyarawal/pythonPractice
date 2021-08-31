""" Minimum Difference between elements: given an array we have to find the minimum difference between two elements
    among all the elements in the array"""
import sys
from quick_sort import quick_sort_hoare

"""Solution"""


def min_difference(arr) -> int:
    min_diff = sys.maxsize
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            min_diff = min(min_diff, abs(arr[i] - arr[j]))
    return min_diff


def min_difference_eff(arr) -> int:
    min_diff = sys.maxsize
    quick_sort_hoare(arr, 0, len(arr)-1)
    for i in range(len(arr)-1):
        min_diff = min(min_diff, abs(arr[i+1]-arr[i]))
    return min_diff


def main():
    arr_input = [8, -1, 0, 3]
    print(arr_input)
    a2 = min_difference(arr_input)
    print(a2)
    a2 = min_difference_eff(arr_input)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
