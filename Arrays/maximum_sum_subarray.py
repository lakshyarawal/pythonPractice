""" Maximum Sum Sub array: Given an array find the max sum from a continuous subset of numbers"""

"""Solution:  """


def max_sub_sum(a) -> int:
    n = len(a)
    res = a[0]
    for i in range(n):
        val = a[i]
        if val > res:
            res = val
        for j in range(i+1, n):
            val = val + a[j]
            if val > res:
                res = val
    return res


def max_sub_sum_eff(a) -> int:
    n = len(a)
    res = a[0]
    max_ending = a[0]
    for i in range(1, n):
        max_ending = max(max_ending + a[i], a[i])
        res = max(max_ending, res)
    return res


def main():
    arr_input = [2, 3, -8, 7, -1, 2, 3]
    a2 = max_sub_sum_eff(arr_input)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
