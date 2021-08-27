""" Insertion Sort Algorithm:"""


"""Implementation"""


def insertion_sort(arr) -> list:
    n = len(arr)
    for i in range(1, n):
        swap_index = i
        for j in range(i-1, -1, -1):
            if arr[swap_index] < arr[j]:
                arr[swap_index], arr[j] = arr[j], arr[swap_index]
                swap_index -= 1
            else:
                break
    return arr


def main():
    arr_input = [10, 5, 30, 1, 2, 5, 10, 10]
    a2 = insertion_sort(arr_input)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
