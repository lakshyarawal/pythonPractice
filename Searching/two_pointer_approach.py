"""Finding peak element: In an unsorted array, find element which is not smaller than it's neighbours"""
from binary_search import binary_search_iterative
""" Solution: """


def peak_element(a) -> int:
    n = len(a)
    if n == 1:
        return a[0]
    if a[0] > a[1]:
        return a[0]
    if a[n-1] > a[n-2]:
        return a[n-1]
    for i in range(1, n-1):
        if a[i] > a[i-1] and a[i] > a[i+1]:
            return a[i]
    return -1


def peak_element_eff(a) -> int:
    n = len(a)
    low = 0
    high = n-1
    while low <= high:
        mid = (low + high) // 2
        if (mid == 0 or a[mid] >= a[mid-1]) and (mid == n-1 or a[mid] >= a[mid+1]):
            return a[mid]
        if mid > 0 and a[mid] < a[mid-1]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def main():
    arr = [10, 20, 15, 5, 23, 90, 67]
    a2 = peak_element_eff(arr)
    print(a2)
    a2 = peak_element(arr)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
