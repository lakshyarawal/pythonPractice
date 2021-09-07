
""" Longest Common Sub array with given sum in two binary arrays of same size"""


def longest_common_sub(arr, arr2) -> int:
    result = 0
    n = len(arr)
    for i in range(n):
        curr_sum1, curr_sum2 = 0, 0
        for j in range(i, n):
            curr_sum1 += arr[j]
            curr_sum2 += arr2[j]
            if curr_sum1 == curr_sum2:
                result = max(result, j-i + 1)
    return result


def long_com(arr, arr2) -> int:
    result = 0
    # Step 1 is to compute the difference array
    temp = [0] * len(arr)
    for i in range(len(arr)):
        temp[i] = arr[i] - arr2[i]
    new_dict = {}
    sum_sub = 0
    new_dict[sum_sub] = 0
    for i in range(len(temp)):
        sum_sub += temp[i]
        if sum_sub in new_dict.keys():
            result = max(result, i+1 - new_dict.get(sum_sub))
        else:
            new_dict[sum_sub] = i + 1
    return result


def main():
    arr_input = [0, 1, 0, 0, 0, 0]
    arr_input2 = [1, 0, 1, 0, 0, 1]
    print(long_com(arr_input, arr_input2))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
