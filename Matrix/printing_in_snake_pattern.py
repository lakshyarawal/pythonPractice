""" Printing in snake pattern: Given a 2D array we have to print it in a snake pattern"""


"""Solution: """


def snake_pattern(arr):
    for i in range(len(arr)):
        if i % 2 == 0:
            for j in range(len(arr[i])):
                print(arr[i][j], end=" ")
        else:
            for j in range(len(arr[i])-1, -1, -1):
                print(arr[i][j], end=" ")


def main():
    arr_input = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    snake_pattern(arr_input)


if __name__ == "__main__":
    main()
