""" More than n/k occurrences """


def distinct_in_window(arr, win_sz) -> list:
    new_dict = {}
    occur = len(arr)//win_sz
    for i in range(len(arr)):
        if arr[i] in new_dict:
            new_dict[arr[i]] += 1
        else:
            new_dict[arr[i]] = 1
    new_dict = {k: v for k, v in new_dict.items() if v > occur}
    result = list(new_dict.keys())
    return result


""" Efficient solution: Lets assume the occurrences of an element is n/k + 1 (Minimum to print) if we have k elements
    in the final result, then K * (N/K + 1) < N which would not hold. Hence max elements in <= K-1"""


def distinct_in_window_eff(arr, win_sz) -> list:
    new_dict = {}
    result = []
    occur = len(arr)//win_sz
    for i in range(len(arr)):
        if arr[i] in new_dict.keys():
            new_dict[arr[i]] += 1
        elif len(new_dict.keys()) < win_sz-1:
            new_dict[arr[i]] = 1
        else:
            new_dict[arr[i]] = 1
            new_dict = {k: v-1 for k, v in new_dict.items() if v != 1}
    for i in new_dict.keys():
        count_curr = 0
        for j in range(len(arr)):
            if i == arr[j]:
                count_curr += 1
        if count_curr > occur:
            result.append(i)
    return result


def main():
    arr_input = [30, 10, 20, 20, 20, 10, 40, 30, 30]
    k = 4
    print(distinct_in_window(arr_input, k))
    print(distinct_in_window_eff(arr_input, k))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
