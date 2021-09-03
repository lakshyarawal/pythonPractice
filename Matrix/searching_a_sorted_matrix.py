""" Searching a sorted matrix: The numbers are sorted row and column wise. Print if input element is found and index """


"""Solution: """


def search_element(arr, val):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] > val:
                break
            if arr[i][j] == val:
                print("Found at: (", i, ", ", j, ")")
                return
    print("Not Found")


def search_element_eff(arr, val):
    i = 0
    j = len(arr) - 1
    while i < len(arr) and -1 < j:
        if arr[i][j] > val:
            j -= 1
            continue
        elif arr[i][j] < val:
            i += 1
            continue
        elif arr[i][j] == val:
            print("Found at: (", i, ", ", j, ")")
            return
        print("Not Found")


def main():
    arr_input = [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]
    search_element_eff(arr_input, 39)


if __name__ == "__main__":
    main()
