""" Prefix Sum Technique: Given a fixed array and  multiple queries of following types on array are to be performed
    how to do it efficiently: I/P: [ 2, 8, 3, 9, 6, 5, 4 ], get_sum(0,2) will return 2+8+3"""

"""Solution:  """


def prefix_sum(a, l, r) -> int:
    prefix_sum_arr = [0] * len(a)
    prefix_sum_arr[0] = a[0]
    for i in range(1, len(a)):
        prefix_sum_arr[i] = prefix_sum_arr[i-1] + a[i]
    if l == 0:
        return prefix_sum_arr[r]
    return prefix_sum_arr[r] - prefix_sum_arr[l-1]


""" Variation: Find if the given array has an equilibrium point in the array, around which 
    the sum is same to the left and right. Eg: 20 in [ 3, 4, 8, -9, 20, 6 ]"""


def eq_point(a) -> bool:
    prefix_sum_arr = [0] * len(a)
    prefix_sum_arr[0] = a[0]
    for i in range(len(a)):
        prefix_sum_arr[i] = prefix_sum_arr[i-1] + a[i]
    postfix_sum_arr = [0] * len(a)
    postfix_sum_arr[0] = a[len(a)-1]
    for i in range(1, len(a)):
        postfix_sum_arr[i] = postfix_sum_arr[i - 1] + a[len(a) - 1 - i]
    print(prefix_sum_arr)
    print(postfix_sum_arr)
    for i in range(len(a)-1):
        if prefix_sum_arr[i-1] == postfix_sum_arr[i+1]:
            return True
    return False


def main():
    arr_input = [3, 4, 8, -9, 20, 6]
    a2 = eq_point(arr_input)
    print(a2)
    a2 = prefix_sum(arr_input, 0, 3)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
