""" lLEXICOGRAPHIC RANK : We have to find count of strings that would appear before this string if placed alphabetically
    in increasing order of permutations of all char of string """
from Mathematics.factorial import factorial


def lexicographic_rank(str_in) -> int:
    rank_final = 0
    n = len(str_in)
    str_arr = []
    for i in range(n):
        str_arr.append(ord(str_in[i]))
    for i in range(n):
        curr_count = 0
        for j in range(i+1, n):
            if str_arr[i] > str_arr[j]:
                curr_count += 1
        fac = factorial(n-i-1)
        rank_final += fac*curr_count
    return rank_final+1


def main():
    str_input = "DCBA"
    print(lexicographic_rank(str_input))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()

