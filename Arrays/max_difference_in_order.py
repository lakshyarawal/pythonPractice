""" Max Difference in Order: Given an array find the max(a[j] - a[i]) such that j>i """

"""Solution:  """


def max_difference(a) -> int:
    n = len(a)
    if n == 1:
        return 0
    curr_max = a[1] - a[0]
    for i in range(n):
        for j in range(i+1, n):
            if a[j] - a[i] > curr_max:
                curr_max = a[j] - a[i]
    return curr_max


def max_difference_eff(a) -> int:
    n = len(a)
    if n == 1:
        return 0
    curr_min = a[0]
    res = a[1] - a[0]
    for i in range(1, n):
        res = max(res, a[i] - curr_min )
        curr_min = min(a[i], curr_min)
    return res


def main():
    arr_input = [2, 3, 10, 6, 4, 8, 1]
    a = max_difference_eff(arr_input)
    print(a)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
