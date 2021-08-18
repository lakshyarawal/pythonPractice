""" Largest Element in Array: Given an array find the largest element in the array """

"""Solution:  """


def largest_element(a) -> int:
    le = 0
    for i in a:
        if i > le:
            le = i
    return le


def main():
    arr_input = [40, 100, 8, 50]
    a = largest_element(arr_input)
    print(a)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
