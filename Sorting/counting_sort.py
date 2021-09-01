""" Count Sort Algorithm: Not a comparison based algorithm, this is useful when elements are present in a small range
    n to n + k where k is comparable or smaller than n"""


"""Implementation"""


def count_sort(arr, k) -> list:
    n = len(arr)
    count = [0] * k
    for i in range(n):
        count[arr[i]] += 1
    print(count)
    for i in range(1, k):
        count[i] = count[i-1] + count[i]
    print(count)
    output = [0] * n
    for i in range(n-1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    return output


def main():
    arr_input = [5, 6, 5, 2]
    k = max(arr_input) + 1
    a2 = count_sort(arr_input, k)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
