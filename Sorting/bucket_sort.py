""" Bucket Sort Algorithm: Where to use it: Numbers are in the range [1 to 10 ^ 8) and they are uniformly distributed in
    this range or we have floating point numbers and they are distributed in the range [0.0 to 1.0)"""
import math

"""Implementation"""


def bucket_sort(arr, b) -> list:
    n = max(arr)  # Maximum element in the array
    n += 1  # To avoid overflow if max element is present
    size = math.ceil(n/b)  # Size of each bucket to determine which bucket element goes into
    buckets = [[] for _ in range(b)]  # How to declare an empty 2D array
    for i in range(len(arr)):
        index = arr[i] // size
        buckets[index].append(arr[i])
    print(buckets)
    output = [0] * len(arr)
    k = 0
    for i in range(b):  # Sorting individual buckets
        buckets[i] = sorted(buckets[i])
    for i in range(b):  # Storing the results in one output array by combining output of each bucket
        for j in range(len(buckets[i])):
            output[k] = buckets[i][j]
            k += 1
    return output


def main():
    arr_input = [30, 40, 10, 80, 5, 12, 70]
    buckets = 4
    a2 = bucket_sort(arr_input, buckets)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
