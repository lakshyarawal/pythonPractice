""" Radix Sort Algorithm: This is an extension of counting sort and is able to sort numbers in a higher range in O(n)
    liner time. 1-step here is to find the number of digits in the max and make the same number of digits in all """


"""Implementation"""


def count_sort(arr, k):
    n = len(arr)
    count = [0] * 10
    for i in range(n):
        count[(arr[i]//k) % 10] += 1
    for i in range(1, 10):
        count[i] = count[i-1] + count[i]
    output = [0] * n
    for i in range(n-1, -1, -1):
        output[count[(arr[i]//k) % 10] - 1] = arr[i]
        count[(arr[i]//k) % 10] -= 1
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr) -> list:
    max_ele = max(arr)
    exp = 1
    while max_ele//exp > 0:
        count_sort(arr, exp)
        exp *= 10
    return arr


def main():
    arr_input = [319, 212, 6, 8, 100, 50]
    a2 = radix_sort(arr_input)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
