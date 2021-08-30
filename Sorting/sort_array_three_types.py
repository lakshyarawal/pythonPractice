""" Sort Array with two types of elements: Positives/Negatives, Even/Odd, Binary Array, we have to put one type of elements
    together. The order among one type of elements is not imp"""

from lomuto_partition import lom_partition

"""Solution"""


def segregate_elements(arr) -> list:
    i = -1
    j = len(arr)
    while True:
        i += 1
        while arr[i] < 0:
            i += 1
        j -= 1
        while arr[j] >= 0:
            j -= 1
        if i >= j:
            return arr
        arr[i], arr[j] = arr[j], arr[i]


def main():
    arr_input = [-12, 10, -18, 9]
    print(arr_input)
    a2 = segregate_elements(arr_input)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
