
""" Sub array with 0 sum """


def find_sum_sub(arr, sum_in) -> bool:
    new_set = set()
    sum_array = 0
    new_set.add(sum_array)
    for i in range(len(arr)):
        if (sum_array - sum_in) in new_set:
            return True
        sum_array += arr[i]
        # Adding the sum of all elements in the set, if there is a 0 sum, total sum will repeat itself
        new_set.add(sum_array)
    return False


def main():
    arr_input = [3, 2, 5, 6]
    sum_input = 10
    print(find_sum_sub(arr_input, sum_input))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
