""" Maximum Sum of a Circular Sub-array: A circular sub-array is when you connect the last element to first
    We have to find sum among all sub arrays, circular and normal"""

"""Solution:  """


def max_circular_sum(a) -> int:
    n = len(a)
    res = a[0]
    for i in range(n):
        curr_max = a[i]
        curr_sum = a[i]
        for j in range(1, n):
            index_ = (i + j) % n
            curr_sum = curr_sum + a[index_]
            curr_max = max(curr_sum, curr_max)
        res = max(res, curr_max)
    return res


def max_circular_sum_eff(a) -> int:
    n = len(a)
    res = a[0]
    max_ending = a[0]
    for i in range(1, n):
        max_ending = max(max_ending + a[i], a[i])
        res = max(max_ending, res)
    normal_res = res
    if normal_res < 0:
        return normal_res
    res = a[0]
    min_ending = a[0]
    total_sum = 0
    for i in range(n):
        total_sum += a[i]
    for i in range(1, n):
        min_ending = min(min_ending + a[i], a[i])
        res = min(min_ending, res)
    circle_res = total_sum - res
    return max(normal_res, circle_res)


def main():
    arr_input = [3,-4, 5, 6, -8, 7]
    a2 = max_circular_sum(arr_input)
    print(a2)
    a3 = max_circular_sum_eff(arr_input)
    print(a3)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
