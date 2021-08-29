""" Hoare's Partition : """


"""Implementation"""


def hoare_partition(arr, low, high) -> int:
    pivot = arr[low]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def main():
    arr_input = [5, 3, 8, 4, 2, 7, 1, 10]
    a2 = hoare_partition(arr_input, 0, 7)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
