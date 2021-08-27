""" Insertion Sort Algorithm:"""


"""Implementation"""


def bubble_sort(arr) -> list:
    n = len(arr)
    for j in range(1, n):
        swapped = True
        for i in range(n-j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = False
        if swapped:
            break
        print(arr)
    return arr


def main():
    arr_input = [10, 5, 30, 1, 2, 5, 10, 10]
    a2 = bubble_sort(arr_input)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
