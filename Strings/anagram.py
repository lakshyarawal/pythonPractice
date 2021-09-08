""" Anagram Check : To see if a given string is permutation of the other string or not """
from collections import Counter

"""Implementation 1: comparing dictionaries of the two strings """


def anagram_check(str_in, str_in2) -> bool:
    dict1 = Counter(str_in)
    dict2 = Counter(str_in2)
    return dict1 == dict2


""" Using character counting technique"""


def anagram_check_count(str_in, str_in2) -> bool:
    if len(str_in) != len(str_in2):
        return False
    count_arr = [0] * 256
    for i in range(len(str_in)):
        count_arr[ord(str_in[i])] += 1
        count_arr[ord(str_in2[i])] -= 1
    for i in count_arr:
        if i != 0:
            return False
    return True


def main():
    str_input = "silent"
    str_input2 = "listen"
    print(anagram_check(str_input, str_input2))
    print(anagram_check_count(str_input, str_input2))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
