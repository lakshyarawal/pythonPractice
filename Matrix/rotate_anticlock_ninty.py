""" Rotating a matrix Anticlockwise by 90 degrees : """


"""Solution: """


def rotate_anti(arr):
    n = len(arr)
    for i in range(len(arr)):
        for j in range(i+1, len(arr[i])):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    for i in range(len(arr)//2):
        for j in range(len(arr[i])):
            arr[i][j], arr[n-i][j] = arr[n-i][j], arr[i][j]
    print(arr)


def main():
    arr_input = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    rotate_anti(arr_input)


if __name__ == "__main__":
    main()
