""" Array Operations: Searching an element in an unsorted array and returning index of it's first occurrence"""

"""Solution: Recursively make calls for string by including and not including character at index I, this will create 
    all combinations in the form of a tree """


def searching_array(a, n) -> int:
    for i in range(len(a)):
        if n == a[i]:
            return i
    return -1


def inserting_element(a, n, index_) -> list:
    for i in range(len(a)-1, index_, -1):
        a[i] = a[i-1]
    a[index_ - 1] = n
    return a


def deleting_element(a, n) -> list:
    a.remove(n)
    return a


def main():
    arr_input = [9, 10, 11, 25, 0, 0]
    num = 25
    ans = searching_array(arr_input, num)
    print(ans)
    ans2 = inserting_element(arr_input, num, 3)
    print(ans2)
    ans3 = deleting_element(arr_input, num)
    print(ans3)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
