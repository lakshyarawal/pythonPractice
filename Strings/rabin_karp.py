""" Rabin Karp Algorithm: we compute a weighted sum hash function to see if pattern matches the current text """


"""Implementation"""


def rb_search(txt, ptr_in, q) -> list:
    res = []  # Array to store all indexes
    d = 256
    m = len(ptr_in)
    n = len(txt)
    p = 0  # hash value for pattern
    t = 0  # hash value for txt
    h = 1

    # The value of h would be "pow(d, m-1)% q"

    for i in range(m - 1):
        h = (h * d) % q

    # Calculate the hash value of pattern and first window
    # of text
    for i in range(m):
        p = (d * p + ord(ptr_in[i])) % q
        t = (d * t + ord(txt[i])) % q

    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters one by one
        if p == t:
            bool_flag = True
            # Check for characters one by one
            for j in range(m):
                if txt[i + j] != ptr_in[j]:
                    bool_flag = False
                    break

            if bool_flag:
                res.append(i)

        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < n - m:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + m])) % q

            # We might get negative values of t, converting it to
            # positive
            if t < 0:
                t = t + q
    return res


def main():
    str_input = "geeksforgeeks"
    ptr_input = "eks"
    print(rb_search(str_input, ptr_input, 17))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
