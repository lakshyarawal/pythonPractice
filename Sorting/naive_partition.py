""" Naive Partition : We are given an array and an index in the array. We have to put all elements smaller than this
    element to left and bigger to the right"""


"""Implementation"""


def naive_partition(arr, low, high, pivot) -> int:
    # Create a temp array
    temp = [0] * (high - low + 1)
    index = 0
    for i in range(low, high+1):
        if arr[i] < arr[pivot]:
            temp[index] = arr[i]
            index += 1
    for i in range(low, high + 1):
        if arr[i] == arr[pivot]:
            temp[index] = arr[i]
            index += 1
    result = low + index - 1
    for i in range(low, high + 1):
        if arr[i] > arr[pivot]:
            temp[index] = arr[i]
            index += 1
    for i in range(low, high + 1):
        arr[i] = temp[i-low]
    return result


def main():
    arr_input = [3, 5, 8, 5]
    a2 = naive_partition(arr_input, 0, 3, 3)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
