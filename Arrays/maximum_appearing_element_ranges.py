""" Given N ranges, find the maximum appearing element in these ranges L: [ 1, 2, 5, 15 ] R: [ 5, 8, 7, 18 ]. Ranges are
    1-5, 2-8, 5-7, 15-18"""

"""Solution:  """


def max_appear(left_array, right_array) -> int:
    n = len(left_array)
    prefix_arr = [0] * 1000
    for i in range(n):
        prefix_arr[left_array[i]] += 1
        prefix_arr[right_array[i]+1] -= 1

    max_elem = prefix_arr[0]
    res = 0
    for i in range(1, len(prefix_arr)):
        prefix_arr[i] += prefix_arr[i-1]
        if max_elem < prefix_arr[i]:
            print(prefix_arr[i])
            max_elem = prefix_arr[i]
            res = i
    return res


""" More related questions: Check if an array can be divided into 3 parts with equal sum
    Check if there exists a sub-array with 0 sum 
    Find the largest sub-array with with equal 0s and 1s in a binary array """


def main():
    left_arr = [1, 2, 5, 15]
    right_arr = [5, 8, 7, 18]
    a2 = max_appear(left_arr, right_arr)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
