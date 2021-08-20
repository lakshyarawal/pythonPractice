""" Maximum Sum of a Circular Sub-array: A circular sub-array is when you connect the last element to first
    We have to find sum among all sub arrays, circular and normal"""

"""Solution:  """


def max_circular_sum_eff(a) -> int:
    n = len(a)
    res = a[0]
    for i in range(1, n):
        res = max(res, a[i] + res)
    return res


def main():
    arr_input = [2, 3, -8, 7, -1, 2, 3]
    a2 = max_circular_sum_eff(arr_input)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
