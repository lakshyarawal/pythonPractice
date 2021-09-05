
""" Counting distinct elements in a given array of numbers """


def count_distinct(arr) -> int:
    new_set = set(arr)
    print(new_set)
    return len(new_set)


def main():
    arr_input = [15, 12, 13, 12, 13, 13, 18]
    print(count_distinct(arr_input))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
