""" Count Occurrences: """
from index_of_last_occurrence import last_occur
from index_of_first_occurrence import first_occur
""" Solution: """


def count_occur(arr, num) -> int:
    low_index = first_occur(arr, num)
    if low_index == -1:
        return 0
    high_index = last_occur(arr, num)
    return (high_index - low_index) + 1


def main():
    arr_input = [1, 10, 10, 10, 20, 20, 20, 20, 20, 40]
    a2 = count_occur(arr_input, 20)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()