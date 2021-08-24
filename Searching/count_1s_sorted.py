""" Count 1s in a sorted binary array: """
from index_of_first_occurrence import first_occur
""" Solution: """


def count_1(arr, num) -> int:
    low_index = first_occur(arr, num)
    if low_index == -1:
        return 0
    return len(arr) - low_index


def main():
    arr_input = [0, 0, 0]
    a2 = count_1(arr_input, 1)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()