""" Kth Smallest Element:"""
from quick_sort import quick_sort_hoare
from lomuto_partition import lom_partition

"""Solution"""


def kth_element(arr, rank) -> int:
    low = 0
    high = len(arr) - 1
    quick_sort_hoare(arr, low, high)
    return arr[rank - 1]


def kth_element_eff(arr, rank) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        p = lom_partition(arr, low, high)
        if p == rank - 1:
            return arr[rank - 1]
        if p > rank - 1:
            high = p - 1
        if p < rank - 1:
            low = p + 1
    return -1


def main():
    arr_input = [30, 20, 5, 10, 8]
    print(arr_input)
    k = int(input("Enter K value: "))
    a2 = kth_element_eff(arr_input, k)
    print(a2)
    a2 = kth_element(arr_input, k)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
