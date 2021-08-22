""" Window Sliding Technique: Given an array of integers and a number k, find the maximum sum of k consecutive numbers
    arr = [ 1, 8, 30, -5, 20, 7 ], k = 3 so the output would be 45 (30 + -5 + 20)"""

"""Solution:  """


def window_slider(a, k) -> int:
    n = len(a)
    res = a[0]
    final_res = a[0]
    for i in range(n-k):
        res = a[i]
        for j in range(i+1, i+k):
            res += a[j]
        final_res = max(final_res, res)
    return final_res


def window_slider_eff(a, k) -> int:
    n = len(a)
    final_res = a[0]
    res = a[0]
    for i in range(1, k):
        res += a[i]
    for j in range(k, n):
        res = res + a[j] - a[(j-k)]
        final_res = max(final_res, res)
    return final_res


""" Given an array of unsorted non negative integers, find if there exists a sub-array that is  equal to given sum"""


def window_slider_variation(a, s) -> bool:
    n = len(a)
    res = a[0]
    m = 0
    for i in range(1, n):

        if res < s:
            res += a[i]
        if res > s:
            res = res - a[m]
            m += 1
        if res == s:
            return True
    return False


""" N-Fibonacci numbers: Given N,M print the first M, N-Fibonacci numbers. where N is the sum of first N elements"""


def window_slider_fib(n, m):
    a = [0]*m
    for i in range(n):
        if i < n-1:
            a[i] = 0
        else:
            a[i] = 1
    print(a)
    a[n] = a[n-1]
    res = a[n]
    for i in range(n+1, m):
        a[i] = res + a[i-1] - a[i-n]
        print(i, res, a[i - 1], a[i - n])
        res = res + a[i-1]
    print(a)


""" Another Varioation: Count distinct elements in the window of size k"""


def main():
    arr_input = [1, 4, 20, 3, 10, 5]
    print(arr_input)
    window_slider_fib(3, 8)
    window_size = int(input("Enter Window Size: "))
    a = window_slider_variation(arr_input, 33)
    print(a)
    a = window_slider_eff(arr_input, window_size)
    print(a)
    a = window_slider(arr_input, window_size)
    print(a)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
