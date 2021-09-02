""" Transpose of a matrix : Given a 2D array we have to print it after exchanging the rows and columns in NxN array"""


"""Solution: """


def transpose(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr[i])):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    print(arr)


def main():
    arr_input = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    transpose(arr_input)


if __name__ == "__main__":
    main()
