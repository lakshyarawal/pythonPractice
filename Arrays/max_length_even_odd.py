""" Maximum Sum Sub array: Given an array find the max sum from a continuous subset of numbers"""

"""Solution:  """


def max_odd_even(a) -> int:
    n = len(a)
    if n == 1:
        return 1
    curr_len = 1
    max_len = 1
    for i in range(1, n):
        if (a[i] % 2 == 0 and a[i-1] % 2 != 0) or (a[i] % 2 != 0 and a[i-1] % 2 == 0):
            curr_len += 1
            max_len = max(curr_len, max_len)
        else:
            curr_len = 1
    return max_len


def main():
    arr_input = [5, 10, 20, 6, 3, 8]
    a2 = max_odd_even(arr_input)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
