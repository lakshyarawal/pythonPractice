""" Selection Sort Algorithm:"""
import sys

"""Implementation"""


def selection_sort(arr) -> list:
    n = len(arr)
    temp = [0] * n
    for i in range(n):
        min_element = sys.maxsize
        min_index = 0
        for j in range(n):
            if arr[j] < min_element:
                min_index = j
                min_element = arr[j]
        temp[i] = (arr[min_index])
        arr[min_index] = sys.maxsize
    return temp


def selection_sort_eff(arr) -> list:
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index],  arr[i]
    return arr


def main():
    arr_input = [10, 5, 30, 1, 2, 5, 10, 10]
    a2 = selection_sort(arr_input)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
