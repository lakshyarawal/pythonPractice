""" Move Zeros to end of Array: Given an array, move all zeros to it's end """

"""Solution:  """


def move_zeros(a) -> list:
    for i in range(len(a)):
        if a[i] == 0:
            for j in range(i+1, len(a)):
                if a[j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
    return a


def move_zeros_linear(a) -> list:
    if len(a) == 1:
        return a
    swap_index = 0
    for i in range(len(a)):
        if a[i] != 0:
            a[i], a[swap_index] = a[swap_index], a[i]
            swap_index += 1
    return a


def main():
    arr_input = [10, 0, 0, 30]
    a = move_zeros(arr_input)
    print(a)
    a2 = move_zeros_linear(arr_input)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
