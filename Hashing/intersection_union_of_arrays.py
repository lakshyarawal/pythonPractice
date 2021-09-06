
""" Intersection and Union of Two Arrays: Another approach would be to create one set and check from other array """


def intersection(arr, arr2) -> int:
    set1 = set(arr)
    set2 = set(arr2)
    print(set1.intersection(set2))
    return len(set1.intersection(set2))


def union(arr, arr2) -> int:
    set1 = set(arr)
    set2 = set(arr2)
    print(set1.union(set2))
    return len(set1.union(set2))


def main():
    arr_input = [10, 12, 10, 15, 10, 20, 12, 12]
    arr_input_2 = [10, 19, 33, 33, 19, 12]
    print(intersection(arr_input, arr_input_2))
    print(union(arr_input, arr_input_2))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
