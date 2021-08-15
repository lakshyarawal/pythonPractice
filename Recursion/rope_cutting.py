""" Rope Cutting Problem:  Given a rope of length N. Calculate how many max no. of pieces can be cut either of length
    A, B, C """

"""Solution:  """


def rope_cutting(n, a, b, c) -> int:
    if n == 0:
        return 0
    if n < 0:
        return -1
    min_num = min(a, b, c)
    if n < min_num:
        return -1
    if n - b == 0 or n - c == 0 or n - a == 0:
        return 1
    option_1 = rope_cutting(n - a, a, b, c)
    option_2 = rope_cutting(n - b, a, b, c)
    option_3 = rope_cutting(n - c, a, b, c)
    res = max(option_1, option_2, option_3)
    if res == -1:
        return -1
    return res + 1


def main():
    val1 = int(input("Enter rope Length: "))
    len_1 = int(input("Enter a number: "))
    len_2 = int(input("Enter a number: "))
    len_3 = int(input("Enter a number: "))
    a = rope_cutting(val1, len_1, len_2, len_3)
    print(a)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
