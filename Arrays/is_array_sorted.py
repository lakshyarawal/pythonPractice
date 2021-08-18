""" Is Array Sorted: Given an array check if the elements are present in sorted order"""

"""Solution:  """


def is_array_sorted(a) -> bool:
    is_sorted = True
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            is_sorted = False
    return is_sorted


def main():
    arr_input = [5, 20, 80, 100]
    a = is_array_sorted(arr_input)
    print(a)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
