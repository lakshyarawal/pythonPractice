
""" Sub array with 0 sum """


def find_zero_sub(arr) -> bool:
    new_set = set()
    sum_array = 0
    new_set.add(sum_array)
    for i in range(len(arr)):
        sum_array += arr[i]
        # Adding the sum of all elements in the set, if there is a 0 sum, total sum will repeat itself
        if sum_array in new_set:
            return True
        new_set.add(sum_array)
    return False


def main():
    arr_input = [1, 4, 13, -3, -10, 5]
    print(find_zero_sub(arr_input))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
