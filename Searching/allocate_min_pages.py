""" Allocating minimum pages: Given an array of values which signifies number of pages a student has to read.
    We have to minimize the maximum number of pages a student has to read given the student count. Eg: [10, 20, 30, 40]
    and k = 2, O/P: 60 ( 30+20+10). A student cannot read discontinuous set of pages"""
import sys

""" Solution: """


def sum_arr(arr, start, end):
    total_sum = 0
    for i in range(start, end):
        total_sum += arr[i]
    return total_sum


def allocate_pages_rec(p, arr_size, s) -> int:
    if s == 1:
        return sum_arr(p, 0, arr_size)
    if arr_size == 1:
        return p[0]
    result = sys.maxsize
    for i in range(arr_size):
        result = min(result, max(allocate_pages_rec(p, i, s-1), sum_arr(p, i, arr_size)))
    return result


def is_feasible(arr, arr_size, students, mid_value):
    req = 1
    arr_sum = 0
    for i in range(arr_size):
        if arr_sum + arr[i] > mid_value:
            req += 1
            arr_sum = arr[i]
        else:
            arr_sum += arr[i]
    return req <= students


def allocate_pages_eff(p, arr_size, s) -> int:
    total_sum, mx = 0, 0
    for i in range(arr_size):
        total_sum += p[i]
        mx = max(mx, p[i])
    low = mx
    high = total_sum
    result = 0
    while low <= high:
        mid = (low + high)//2
        if is_feasible(p, arr_size, s, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result


def main():
    pages = [10, 5, 30, 1, 2, 5, 10, 10]
    students = 3
    n = len(pages)
    a2 = allocate_pages_eff(pages, n, students)
    print(a2)
    a2 = allocate_pages_rec(pages, n, students)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
