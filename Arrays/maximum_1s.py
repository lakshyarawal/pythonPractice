""" Maximum 1s in a binary array: In a given binary array find the largest continuous set of 1s in the array """

"""Solution:  """


def max_ones(a) -> int:
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
    arr_input = [1, 0, 1, 1, 1,0, 1, 1, 1, 1]
    a2 = max_ones(arr_input)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
