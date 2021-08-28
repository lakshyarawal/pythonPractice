""" Merge Sort Algorithm: Divide and Conquer approach using the merge function """


"""Implementation"""


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if right > left:
        mid = left + (right - left)//2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)
        merge(arr, left, mid, right)


def main():
    arr_input = [5, 4, 3, 2, 1]
    left_input = 0
    right_input = len(arr_input) - 1
    merge_sort(arr_input, left_input, right_input)
    print(arr_input)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
