
""" Counting frequency of  elements in a given array of numbers """


def frequency_elements(arr) -> int:
    new_dict = dict()
    for i in range(len(arr)):
        if arr[i] in new_dict:
            new_dict[arr[i]] += 1
        else:
            new_dict[arr[i]] = 1
    print(new_dict)
    return len(new_dict)


def main():
    arr_input = [10, 12, 10, 15, 10, 20, 12, 12]
    print(frequency_elements(arr_input))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
