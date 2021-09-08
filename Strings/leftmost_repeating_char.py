""" Left Most Character that repeats:  """
import sys

"""Implementation: Adding occurrences in the count array and then iterating string to see which one has 2 or more """


def leftmost_repeat_char(str_in) -> int:
    count = [0] * 256
    for i in range(len(str_in)):
        count[ord(str_in[i])] += 1
    for i in range(len(str_in)):
        if count[ord(str_in[i])] > 1:
            print(str_in[i])
            return i
    return -1


""" Efficient: in the count array we store the first index of each element"""


def leftmost_repeat_char_one(str_in) -> int:
    count = [-1] * 256
    res = sys.maxsize
    for i in range(len(str_in)):
        if count[ord(str_in[i])] == -1:
            count[ord(str_in[i])] = i
        else:
            res = min(res, count[ord(str_in[i])])
    if res == sys.maxsize:
        return -1
    else:
        return res


""" Iterating from the right side as well"""


def leftmost_repeat_char_right(str_in) -> int:
    count = [False] * 256
    res = -1
    for i in range(len(str_in)-1, -1, -1):
        if count[ord(str_in[i])]:
            res = i
        else:
            count[ord(str_in[i])] = True
    return res


def main():
    str_input = "geeksforgeeks"
    print(leftmost_repeat_char(str_input))
    print(leftmost_repeat_char_one(str_input))
    print(leftmost_repeat_char_right(str_input))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
