""" Lomuto Partition : We are given an array and we have to put all elements smaller than this element to left and
    bigger to the right. We assume that the pivot is always the last element in the array
    If we are given a pivot element we can swap the pivot ad high to use this algorithm"""


"""Implementation"""


def lom_partition(arr, low, high) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    print(arr)
    return i + 1


def main():
    arr_input = [30, 40, 20, 50, 80]
    a2 = lom_partition(arr_input, 0, 4)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
