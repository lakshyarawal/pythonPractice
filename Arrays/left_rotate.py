""" Left Rotate by 1:  """

"""Solution:  """


def left_rotate(a) -> list:
    temp = a[0]
    n = len(a)
    for i in range(n-1):
        a[i] = a[i+1]
    a[n - 1] = temp
    return a


def left_rotate_by_d(a, d) -> list:
    temp = []
    for i in range(d):
        temp.append(a[i])
    n = len(a)
    for i in range(n-d):
        a[i] = a[i+d]
    m = 0
    for i in range(n-d, n):
        a[i] = temp[m]
        m += 1
    return a


def left_rotate_by_d_no_space(a, d) -> list:
    n = len(a)
    reverse(a, 0, d-1)
    reverse(a, d, n-1)
    reverse(a, 0, n-1)
    return a


def reverse(a, l, h):
    while l < h:
        a[l], a[h] = a[h], a[l]
        l += 1
        h -= 1


def main():
    arr_input = [10, 20, 30, 40, 50]
    diff = int(input("Enter amount to shift by: "))
    a3 = left_rotate_by_d_no_space(arr_input, diff)
    print("result:", a3)
    """a2 = left_rotate_by_d(arr_input, diff)
    print(a2)
    a = left_rotate(arr_input)
    print(a)"""



# Using the special variable
# __name__
if __name__ == "__main__":
    main()
