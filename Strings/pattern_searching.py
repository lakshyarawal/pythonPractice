""" Anagram Check : To see if a given string is permutation of the other string or not """


def pattern_searching(txt_in, ptr_in) -> list:
    res = []
    for i in range(len(txt_in) - len(ptr_in) + 1):
        count = 0
        for j in range(len(ptr_in)):
            if txt_in[i+j] == ptr_in[j]:
                count += 1
        if count == len(ptr_in):
            res.append(i)
    if len(res) == 0:
        print("Not Present")
    return res


def main():
    txt = "ABCABCD"
    ptr = "ABD"
    print(pattern_searching(txt, ptr))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
