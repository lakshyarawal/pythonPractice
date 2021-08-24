""" Search in a sorted rotate array:  [10, 20, 30, 40, 50, 8, 9] is a sorted array rotated 2 times and hence 8,9 come
    in the end. """

""" Solution: """


def rotated_search(a, num) -> int:
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == num:
            return mid
        if a[mid] > a[low]:
            if a[low] <= num < a[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if a[mid] < num <= a[high]:
                low = mid + 1
            else:
                high = mid - 1


def main():
    num_input = int(input("Enter a number here: "))
    arr = [10, 20, 30, 40, 50, 8, 9]
    a2 = rotated_search(arr, num_input)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
