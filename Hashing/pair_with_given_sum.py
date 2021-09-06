
""" Pair with given sum """


def find_pair(arr, sum_in) -> bool:
    new_set = set()
    for i in range(len(arr)):
        if arr[i] in new_set:
            return True
        new_set.add(sum_in - arr[i])
    return False


def main():
    arr_input = [3, 2, 8, 15, -8]
    sum_input = 17
    print(find_pair(arr_input, sum_input))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
