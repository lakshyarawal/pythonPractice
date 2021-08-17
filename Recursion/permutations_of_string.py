""" Permutations of a String: Given a string print all the permutations of it (Different orders of Characters
    Eg: Id S = "ABC" then permutations are: ABC, ACB, BAC, BCA, CBA, CAB (For n there are n! permutations)"""

"""Solution: """


def to_string(list_):
    return ''.join(list_)


def permutations_string(s, i):
    if i == (len(s) - 1):
        print(to_string(s))
        return
    for j in range(i, len(s)):
        s[i], s[j] = s[j], s[i]
        permutations_string(s, i+1)
        s[j], s[i] = s[i], s[j]


def main():
    string_input = input("Enter initial string: ")
    index = 0
    permutations_string(list(string_input), index)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
