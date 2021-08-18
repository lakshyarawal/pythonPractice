""" Removing duplicates from a sorted array: Given an array remove all duplicates and return unique elements """

"""Solution:  """


def remove_duplicates(a) -> int:
    index_ = 1
    for i in range(1, len(a)):
        if a[index_ - 1] != a[i]:
            a[index_] = a[i]
            index_ += 1
    print(a)
    return index_


def main():
    arr_input = [10, 10, 10, 20, 20, 30, 30]
    a = remove_duplicates(arr_input)
    print(a)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
