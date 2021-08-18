""" Reversing an array: Given an array return an array in reverse order """

"""Solution:  """


def reverse_array(a) -> list:
    for i in range(len(a)//2):
        a[len(a) - (1 + i)], a[i] = a[i], a[len(a) - (1 + i)]
    return a


def main():
    arr_input = [20, 80, 100]
    a = reverse_array(arr_input)
    print(a)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
