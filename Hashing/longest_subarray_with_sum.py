
""" Longest Sub array with given sum """


def longest_sum_sub(arr, sum_in) -> int:
    new_dict = {}
    sum_array = 0
    result = 0
    new_dict[sum_array] = 0
    for i in range(len(arr)):
        sum_array += arr[i]
        if sum_array - sum_in in new_dict.keys():
            result = max(result, i+1 - new_dict.get(sum_array-sum_in))
        if sum_array not in new_dict:
            new_dict[sum_array] = i + 1
    return result


def main():
    arr_input = [8, 3, 1, 5, -6, 6, 2, 2]
    sum_input = 4
    print(longest_sum_sub(arr_input, sum_input))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
