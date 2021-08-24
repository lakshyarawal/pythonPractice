""" Find the Index of last Occurrence in a sorted array with duplicates.
    Eg: I/P [ 1, 10, 10, 10, 20, 20, 20, 40 ] , 20 O/P: 6 """

""" Solution: """


def last_occur(arr, num) -> int:
    high = len(arr)-1
    low = 0
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == num:
            if mid == len(arr) - 1 or arr[mid+1] != num:
                return mid
            else:
                low = mid + 1
        if arr[mid] > num:
            high = mid - 1
        if arr[mid] < num:
            low = mid + 1
    return -1


def main():
    arr_input = [1, 10, 10, 10, 20, 20, 20, 40]
    a2 = last_occur(arr_input, 20)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()