""" Pattern Searching : To see if a given string pattern exists in the given text """


def pattern_searching(txt_in, ptr_in) -> list:
    res = []
    for i in range(len(txt_in) - len(ptr_in) + 1):
        for j in range(len(ptr_in)):
            if txt_in[i+j] != ptr_in[j]:
                break
            if j == len(ptr_in) - 1:
                res.append(i)
    if len(res) == 0:
        print("Not Present")
    return res


""" Improvement for distinct elements: """


def pattern_searching_dist(txt_in, ptr_in) -> list:
    res = []
    i = 0
    while i < len(txt_in) - len(ptr_in) + 1:
        j = 0
        for j in range(len(ptr_in)):
            if txt_in[i+j] != ptr_in[j]:
                break
        if j == len(ptr_in) - 1:
            res.append(i)
        if j == 0:
            i += 1
        else:
            i += j
    if len(res) == 0:
        print("Not Present")
    return res



def main():
    txt = "geeksforgeeks"
    ptr = "eks"
    print(pattern_searching(txt, ptr))
    print(pattern_searching_dist(txt, ptr))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
