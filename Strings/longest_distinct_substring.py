""" Longest Substring with Distinct Characters: """


def substring_dist(str_in) -> int:
    prev = [-1] * 256
    j = 0
    res = 0
    for i in range(len(str_in)):
        j = max(j, prev[ord(str_in[i])] + 1)
        max_end = i-j + 1
        res = max(res, max_end)
        prev[ord(str_in[i])] = i
    return res


def main():
    str_input = "abcadbd"
    print(substring_dist(str_input))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
