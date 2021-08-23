""" Find the Index of first Occurrence in a sorted array with duplicates.
    Eg: I/P [ 1, 10, 10, 10, 20, 20, 40 ] O/P: 4 """

""" Solution: """


def binary_search_iterative(arr, num) -> int:
    high = len(arr)
    low = 0
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == num:
            if mid == 0 or arr[mid-1] != num:
                return mid
            else:
                high = mid - 1
        if arr[mid] > num:
            high = mid - 1
        if arr[mid] < num:
            low = mid + 1
    return -1


def main():
    arr_input = [1, 10, 10, 10, 20, 20, 40]
    a2 = binary_search_iterative(arr_input, 20)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()