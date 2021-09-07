""" Count Distinct Elements in Each Window: We are given an array and a number k (k<=n).
    We need to find distinct elements in each k sized window in this array"""


def distinct_in_window(arr, win_sz) -> list:
    result = []
    curr_dict = dict()
    for i in range(win_sz):
        if arr[i] in curr_dict.keys():
            curr_dict[arr[i]] += 1
        else:
            curr_dict[arr[i]] = 1
    result.append(len(curr_dict.keys()))
    m = 0
    for i in range(win_sz, len(arr)):
        curr_dict[arr[m]] -= 1
        if arr[i] in curr_dict.keys():
            curr_dict[arr[i]] += 1
        else:
            curr_dict[arr[i]] = 1
        m += 1
        curr_dict = {k: v for k, v in curr_dict.items() if v != 0}
        result.append(len(curr_dict.keys()))
    return result


def main():
    arr_input = [10, 20, 20, 10, 30, 40, 10]
    k = 4
    print(distinct_in_window(arr_input, k))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
