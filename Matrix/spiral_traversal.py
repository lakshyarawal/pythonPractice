""" Spiral traversal of a matrix : """


"""Solution: """


def spiral(arr, row_start, row_end, col_start, col_end):
    n = len(arr)
    i, j = 0, 0
    while -1 < i < (row_end-row_start) and -1 < j < (col_end-col_start):
        print(arr[i][j], end=" ")
        if i == 1 and j == 0:
            spiral(arr, 1, n-1, 1, n-1)
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
    arr_input = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    start = 0
    end = len(arr_input)
    spiral(arr_input, start, end, start, end)


if __name__ == "__main__":
    main()
