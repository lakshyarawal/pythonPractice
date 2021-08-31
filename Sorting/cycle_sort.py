""" Cycle sort: Has wort time O(n^2) and does the least memory writes and can be useful when memory is costly.
    It is an inplace algorithm which is not stable. Useful for question like min swaps to sort an array """


"""Implementation"""


def cycle_sort(arr) -> list:
    n = len(arr)
    for cs in range(n-1):
        item = arr[cs]
        pos = cs
        for i in range(cs+1, n):
            if arr[cs] > arr[i]:
                pos += 1
            item, arr[pos] = arr[pos], item
        while pos != cs:
            pos = cs
            for i in range(cs+1, n):
                if arr[i] < item:
                    pos += 1
            item, arr[pos] = arr[pos], item
    return arr


def main():
    arr_input = [10, 20, 50, 30, 40]
    a2 = cycle_sort(arr_input)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
