""" Second Largest Element in Array: Given an array find the second largest element in the array """

"""Solution:  """


def second_largest_element(a) -> int:
    le = 0
    sl = -1
    for i in a:
        if i > le:
            le = i
    for i in a:
        if i > sl and i < le:
            sl = i
    return sl


def second_largest_eff(a) -> int:
    le = -1
    res = -1
    for i in a:
        if i > le:
            res = le
            le = i
        else:
            if i > res and i < le:
                res = i
    return res


def main():
    arr_input = [10, 10, 10, 9]
    a = second_largest_element(arr_input)
    print(a)
    a2 = second_largest_eff(arr_input)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
