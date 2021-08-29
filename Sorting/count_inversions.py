""" Count inversions in an array" A pair of elements are called inversion if i < j and arr[i] > arr[j]
    Eg: [2, 4, 1, 3, 5] O/P: 3 ( [2,1], [4,1], [4,3] )"""


"""Solution"""


def count_inversions(arr) -> int:
    n = len(arr)  # length of the array
    inversion_count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                inversion_count += 1
    return inversion_count


def count_merge(arr, l, m, r):
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
    count = 0
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            count = count + n1 - i  # This modification in the merge function helps us count inversions
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
    return count


def count_inversions_eff(arr, left, right) -> int:
    inversion_count = 0
    if left < right:
        mid = left + (right-left)//2
        inversion_count += count_inversions_eff(arr, left, mid)
        inversion_count += count_inversions_eff(arr, mid+1, right)
        inversion_count += count_merge(arr, left, mid, right)
    return inversion_count


def main():
    arr_input = [2, 4, 1, 3, 5]
    n = len(arr_input) - 1
    a2 = count_inversions(arr_input)
    print(a2)
    a2 = count_inversions_eff(arr_input, 0, n)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()

