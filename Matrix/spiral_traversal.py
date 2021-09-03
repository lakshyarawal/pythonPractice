""" Spiral traversal of a matrix : """


"""Solution: """


def spiral(arr):
    top, left = 0, 0
    bottom, right = len(arr) - 1, len(arr) - 1
    while top <= bottom and left <= right:
        for i in range(left, right+1):
            print(arr[top][i], end=" ")
        top += 1
        for i in range(top, bottom+1):
            print(arr[i][right], end=" ")
        right -= 1
        if top <= bottom:
            for i in range(right, left-1, -1):
                print(arr[bottom][i], end=" ")
            bottom -= 1
        if left <= right:
            for i in range(bottom, top-1, -1):
                print(arr[i][left], end=" ")
            left += 1


def main():
    arr_input = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    spiral(arr_input)


if __name__ == "__main__":
    main()
