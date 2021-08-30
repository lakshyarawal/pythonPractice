""" Sort Array with three types of elements: You are given three types of elements in the array and you have to
    sort them accordingly"""


"""Solution"""


def segregate_elements_three(arr) -> list:
    i = 0
    j = len(arr)-1
    mid = 0
    while mid <= j:
        if arr[mid] == 0:
            arr[i], arr[mid] = arr[mid], arr[i]
            i += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[j] = arr[j], arr[mid]
            j -= 1
    return arr


def main():
    arr_input = [0, 2, 1, 0, 0, 2, 1]
    print(arr_input)
    a2 = segregate_elements_three(arr_input)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
