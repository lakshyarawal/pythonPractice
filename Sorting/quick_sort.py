""" Quick Sort Algorithm: Divide and Conquer algorithm by pivoting around element and dividing problem into sub parts
    In this code, it will be implemented using the Lomuto and Hoare's Partition Algorithms"""
from lomuto_partition import lom_partition
from hoare_partition import hoare_partition

"""Implementation"""


def quick_sort_lom(arr, low, high) -> list:
    if low < high:
        p = lom_partition(arr, low, high)
        quick_sort_lom(arr, low, p-1)
        quick_sort_lom(arr, p+1, high)
    return arr


def quick_sort_hoare(arr, low, high) -> list:
    if low < high:
        p = hoare_partition(arr, low, high)
        quick_sort_lom(arr, low, p)
        quick_sort_lom(arr, p+1, high)
    return arr


def main():
    arr_input = [10, 5, 30, 1, 2, 5, 10, 10]
    a2 = quick_sort_hoare(arr_input, 0, 7)
    print(a2)
    a2 = quick_sort_lom(arr_input, 0, 7)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
