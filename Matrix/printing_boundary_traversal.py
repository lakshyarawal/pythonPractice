""" Printing Boundary Traversal pattern: Given a 2D array we have to print it in a snake pattern"""


"""Solution: """


def boundary_traversal(arr):
    i, j = 0, 0
    while -1 < i < len(arr) and -1 < j < len(arr[i]):
        print(arr[i][j])
        if i == 1 and j == 0:
            break
        if i != 0 and j == 0:
            i -= 1
            continue
        if i == len(arr) - 1:
            j -= 1
            continue
        if j == len(arr[i]) - 1:
            i += 1
            continue
        j += 1


def main():
    arr_input = [[1], [2], [3], [4]]
    boundary_traversal(arr_input)


if __name__ == "__main__":
    main()
