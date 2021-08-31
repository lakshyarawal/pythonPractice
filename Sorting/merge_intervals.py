""" Merge Intervals: """

"""Solution"""


def merge_intervals(arr) -> list:
    for i in range(len(arr)):
        low = arr[i][0]
        high = arr[i][1]
        for j in range(i+1, len(arr)):
            curr_low = arr[j][0]
            curr_high = arr[j][1]
            if low <= curr_low <= high or low <= curr_high <= high:
                arr[i] = [-1, -1]
                arr[j] = [min(low, curr_low), max(high, curr_high)]
            elif curr_low <= low <= curr_high or curr_low <= high <= curr_high:
                arr[i] = [-1, -1]
                arr[j] = [min(low, curr_low), max(high, curr_high)]
    return arr


""" Efficient Solution: Sort the elements in the increasing order of start time or decreasing order of end time. """


def merge_intervals_eff(arr) -> list:
    n = len(arr)
    arr = sorted(arr, key=lambda x: x[0])  # This line sorts the 2D array by the first element
    res = 0  # Maintains latest updated interval
    for i in range(1, n):
        if arr[res][1] >= arr[i][0]:
            arr[res][0] = min(arr[i][0], arr[res][0])
            arr[res][1] = max(arr[i][1], arr[res][1])
        else:
            res += 1
            arr[res] = arr[i]
    arr = arr[:res+1]
    return arr


def main():
    arr_input = [[7, 9], [6, 10], [4, 5], [1, 3], [2, 4]]
    print(arr_input)
    a2 = merge_intervals_eff(arr_input)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
