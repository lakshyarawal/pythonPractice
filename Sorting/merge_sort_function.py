""" Merge Sort Algorithm: Divide and Conquer Algorithm"""


"""Implementation: Merging two sorted arrays"""


def merge_sort(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    index1, index2 = 0, 0
    while index1 < n1 and index2 < n2:
        if arr1[index1] <= arr2[index2]:
            print(arr1[index1], end=" ")
            index1 += 1
        else:
            print(arr2[index2], end=" ")
            index2 += 1
    while index1 < n1:
        print(arr1[index1], end=" ")
        index1 += 1
    while index2 < n2:
        print(arr2[index2], end=" ")
        index2 += 1


""" Merge function of merge sort """


def merge_func(arr, low, mid, high) -> list:
    n1 = mid - low + 1
    n2 = high - mid
    left = [0] * n1
    right = [0] * n2
    for i in range(n1):
        left[i] = arr[low+i]
    for j in range(n2):
        right[j] = arr[mid+j+1]
    index1, index2, index3 = 0, 0, 0
    while index1 < n1 and index2 < n2:
        if left[index1] <= right[index2]:
            arr[index3] = left[index1]
            index1 += 1
        else:
            arr[index3] = right[index2]
            index2 += 1
        index3 += 1
    while index1 < n1:
        arr[index3] = left[index1]
        index3 += 1
        index1 += 1
    while index2 < n2:
        arr[index3] = right[index2]
        index3 += 1
        index2 += 1
    return arr


def main():
    arr_input = [1, 2, 5, 10]
    arr_input2 = [3, 4, 8, 9]
    arr_input3 = [5, 8, 12, 14, 7]
    #merge_sort(arr_input, arr_input2)
    print("")
    a2 = merge_func(arr_input3, 0, 3, 4)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
