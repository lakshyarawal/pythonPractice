
""" Longest Sub array with given sum """
from longest_subarray_with_sum import longest_sum_sub


def longest_bin_sub(arr) -> int:
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = -1
    result = longest_sum_sub(arr, 0)
    return result


def main():
    arr_input = [0, 1, 1, 1, 1, 1, 0, 0, 0]
    print(longest_bin_sub(arr_input))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
