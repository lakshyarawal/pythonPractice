""" KMP Algorithm: We have to find the proper prefix of the string input.
    Eg: proper prefix of 'abc' is '', 'a', 'ab' and Suffixes are: '', 'c', 'bc', 'abc' """


""" Naive Implementation : This uses a function to fill LPS array for all substrings by calling prop-prefix function
    Which in turn compares all length of strings from n-1 to 0 to see if any match with prefix and suffix. O(n^3)"""


def prop_prefix(str_in, n) -> int:
    for l_i in range(n-1, 0, -1):
        bool_flag = True
        for i in range(l_i):
            if str_in[i] != str_in[n-l_i+i]:
                bool_flag = False
        if bool_flag:
            return l_i
    return 0


def fill_lps(str_in, lps) -> list:
    for i in range(len(str_in)):
        lps[i] = prop_prefix(str_in, i+1)
    return lps


""" Efficient Method: This uses the LPS value of n-1 to calculate new value O(n). If str[i] is equal to str[len] where
    len is the new last character than we add one to the lps value (lps += 1). if they are not equal if len = 0, lps = 0
    if len != 0 then we find len as lps[len-1] to find the last matching substring that can add the new character to 
    create the new len """


def fill_lps_eff(str_in, lps) -> list:
    n = len(str_in)
    len_ = 0
    lps[0] = 0
    i = 1
    while i < n:
        if str_in[i] == str_in[len_]:
            len_ += 1
            lps[i] = len_
            i += 1
        else:
            if len_ == 0:
                lps[i] = 0
                i += 1
            else:
                len_ = lps[len_ - 1]
    return lps


def kmp(txt_in, ptr_in) -> list:
    res = []
    n = len(txt_in)
    m = len(ptr_in)
    lps_arr = [0] * m
    lps_arr = fill_lps_eff(ptr_in, lps_arr)
    i, j = 0, 0
    while i < n:
        if ptr_in[j] == txt_in[i]:
            i += 1
            j += 1
        if j == m:
            res.append(i-j)
            j = lps_arr[j-1]
        elif i < n and ptr_in[j] != txt_in[i]:
            if j == 0:
                i += 1
            else:
                j = lps_arr[j-1]
    return res


def main():
    str_input = "abbabb"
    pattern_input = "abb"
    lps_input = [0] * len(str_input)
    print(fill_lps(str_input, lps_input))
    print(kmp(str_input, pattern_input))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
