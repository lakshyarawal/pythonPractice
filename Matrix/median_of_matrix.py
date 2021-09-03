""" Median of a Matrix : Given Odd number of elements and all are distinct. We have to print the median.
    The rows are sorted in ascending order"""
from bisect import bisect_right as upper_bound

"""Solution: """


def binary_median(m, r, d):
    mi = m[0][0]
    mx = 0
    for i in range(r):
        if m[i][0] < mi:
            mi = m[i][0]
        if m[i][d - 1] > mx:
            mx = m[i][d - 1]

    desired = (r * d + 1) // 2
    while mi < mx:
        mid = mi + (mx - mi) // 2
        place = 0
        for i in range(r):
            j = upper_bound(m[i], mid)
            print("J: ", j, "M[i] ", m[i], "Mid:", mid)
            place = place + j
            print("Place: ", place, "Desired", desired)
        if place < desired:
            mi = mid + 1
        else:
            mx = mid
    print("Median is", mi)
    return


def main():
    arr_input = [[1, 10, 20], [15, 25, 35], [5, 30, 40]]
    binary_median(arr_input, 3, 3)


if __name__ == "__main__":
    main()
