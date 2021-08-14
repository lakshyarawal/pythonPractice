""" Power Set: For a given string list out all the variations that the string can be represented into
    s = abc, power set = [  , a, b, c, ab, ac, bc, abc ]"""


""" Another Solution: Create All combination of bits and use a counter variable to AND it with the string character """


def power_set_eff(a) -> list:
    power_list_eff = []
    length_list = 1 << len(a)
    for i in range(length_list):
        string_new = ''
        for j in range(len(a)):
            num = 1 << j
            if i & num != 0:
                string_new = string_new + a[j]
        power_list_eff.append(string_new)
    print(len(power_list_eff))
    return power_list_eff


def main():
    string_input = input("Enter string : ")
    ans_eff = power_set_eff(string_input)
    print(ans_eff)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
