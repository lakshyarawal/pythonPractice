"""Median of two sorted arrays: You are given two arrays, you have to find the median after combining the two arrays
    Eg: [10, 20, 30, 40, 50] [5, 15, 25, 35, 45] Combined: [5, 10, 15, 20, *25*, *30*, 35, 40, 45, 50] Median: 27.5"""
import sys

""" Solution: """


def median_arrays(a, b) -> int:
    n = len(a)
    m = len(b)
    new_arr = []
    for i in range(n):
        new_arr.append(a[i])
    for j in range(m):
        new_arr.append(b[j])
    new_arr.sort()
    print(new_arr)
    if (n+m) % 2 != 0:
        return new_arr[(n+m)//2]
    else:
        return (new_arr[(n+m)//2] + new_arr[(n+m)//2-1])/2


def median_arrays_eff(a, b) -> int:
    n1 = len(a)
    n2 = len(b)
    begin1 = 0
    end1 = n1
    while begin1 <= end1:
        i1 = (begin1 + end1) // 2
        i2 = ((n1 + n2 + 1) // 2) - i1
        # min1 is the beginning element in the right side of a
        if i1 == n1:
            min1 = sys.maxsize
        else:
            min1 = a[i1]
        # max1 is the largest(right most) element in the left side of a
        if i1 == 0:
            max1 = -1*sys.maxsize
        else:
            max1 = a[i1-1]
        # min2 is the beginning element in the right side of b
        if i2 == n2:
            min2 = sys.maxsize
        else:
            min2 = b[i2]
        # max2 is the largest(right most) element in the left side of b
        if i2 == 0:
            max2 = -1*sys.maxsize
        else:
            max2 = b[i2-1]
        if max1 <= min2 and max2 <= min1:
            if (n1+n2) % 2 == 0:
                return (max(max2, max1) + min(min2, min1))/2
            else:
                return max(max1, max2)
        elif max1 > min2:
            end1 = i1 - 1
        else:
            begin1 = i1 + 1
    return n1


def main():
    arr = [30, 40, 50, 60]
    arr2 = [5, 6, 7, 8, 9]
    a2 = median_arrays_eff(arr, arr2)
    print(a2)
    a2 = median_arrays(arr, arr2)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
