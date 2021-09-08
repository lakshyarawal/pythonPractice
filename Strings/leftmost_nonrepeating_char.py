""" Left Most Character that does not repeat:  """
import sys

"""Implementation"""


def leftmost_non_repeat_char(str_in) -> int:
    count = [-1] * 256
    res = sys.maxsize
    for i in range(len(str_in)):
        if count[ord(str_in[i])] == -1:
            count[ord(str_in[i])] = i
        else:
            count[ord(str_in[i])] = -2
    for i in count:
        if i > -1:
            res = min(res, i)
    return res


def main():
    str_input = "apple"
    print(leftmost_non_repeat_char(str_input))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
