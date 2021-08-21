""" Maximum Consecutive Flips: In a binary array """

"""Solution:  """


def max_flips(a) -> int:
    n = len(a)
    count_zeros = 0
    for i in range(n):
        if a[i] == 0:
            count_zeros += 1
    count_ones = n - count_zeros
    for i in range(n):
        if count_ones >= count_zeros and a[i] != 1:
            a[i] = 1
            print(i, " to 1")
        elif count_ones < count_zeros and a[i] != 0:
            a[i] = 0
            print(i, " to 0")
    return n


def max_flips_eff(a) -> int:
    n = len(a)
    res = 0
    final_res = 0
    for i in range(n):
        if a[i] == 0:
            res = 0
        else:
            res += 1
            final_res = max(res, final_res)
    return final_res


def main():
    arr_input = [0, 1]
    a2 = max_flips(arr_input)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
