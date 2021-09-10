""" Anagram Pattern Check : To see if a given string is permutation of substring in the other string or not """


def compare(arr1, arr2):
    for i in range(256):
        if arr1[i] != arr2[i]:
            return False
    return True


def anagram_pattern(str_in, str_in2) -> bool:
    count_arr = [0] * 256
    count_ptr = [0] * 256
    for i in range(len(str_in2)):
        count_arr[ord(str_in[i])] += 1
        count_ptr[ord(str_in2[i])] += 1
    for i in range(len(str_in2), len(str_in)):
        if compare(count_ptr, count_arr):
            print("Found at Index", (i - len(str_in2)))
            return True
        count_arr[ord(str_in[i])] += 1
        count_arr[ord(str_in[i-len(str_in2)])] -= 1
    return False


def main():
    str_input = "geeksforgeeks"
    str_input2 = "forg"
    print(anagram_pattern(str_input, str_input2))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
