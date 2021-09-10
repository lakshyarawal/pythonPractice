""" Rotation Check : To see if a given string is rotation of another string or not """
from kmp_proper_prefix import kmp

"""Implementation"""


def rotation_check(str_in, str_in2) -> bool:
    if len(str_in) != len(str_in2):
        return False
    if str_in == str_in2:
        return True
    s1 = list(str_in)
    s2 = list(str_in2)
    print(s1, s2)
    j = 0
    while j < len(s2):
        temp = s2[0]
        for i in range(len(s2)-1):
            s2[i] = s2[i+1]
        s2[len(s2)-1] = temp
        if s1 == s2:
            return True
        j += 1
    return False


""" We concatenate the string 1 with itself and then search using library functions """


def rotation_eff(str_in, str_in2) -> bool:
    if len(str_in) != len(str_in2):
        return False
    if str_in == str_in2:
        return True
    str_in += str_in
    bool_flag = str_in.find(str_in2)
    return bool_flag


def main():
    str_input = "ABAAA"
    str_input2 = "BBAAA"
    print(rotation_check(str_input, str_input2))
    print(rotation_eff(str_input, str_input2))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
