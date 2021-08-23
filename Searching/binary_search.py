
""" Binary Search: Iterative and Recursive with an analysis (O(log n))"""

"""Solution:  """


def binary_search_iterative(arr, num) -> int:
    high = len(arr)
    low = 0
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == num:
            return mid
        if arr[mid] > num:
            high = mid - 1
        if arr[mid] < num:
            low = mid + 1
    return -1


def binary_search_recursive(arr, num, high, low) -> int:
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == num:
        return mid
    if arr[mid] > num:
        return binary_search_recursive(arr, num, mid - 1, low)
    if arr[mid] < num:
        return binary_search_recursive(arr, num, high, mid + 1)
    return -1


def main():
    arr_input = [5, 10, 15, 20, 25, 35]
    a2 = binary_search_iterative(arr_input, 25)
    print(a2)
    a3 = binary_search_recursive(arr_input, 25, len(arr_input), 0)
    print(a3)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
