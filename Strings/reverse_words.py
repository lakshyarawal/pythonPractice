""" Reverse Words in a string:  """


"""Implementation : Using a array to store words and then creating a new string to reverse"""


def reverse_words(str_in) -> str:
    str_final = str_in.split(" ")
    str_in = ""
    for i in range(len(str_final)-1, 0, -1):
        str_in += str_final[i] + " "
    str_in += str_final[0]
    return str_in


"""Implementation : Reversing the array multiple times(first words) then array to achieve the output"""


# Python3 program to reverse a string

# Function to reverse each word in the string
def reverse_word(s, low, high):
    while low < high:
        s[low], s[high] = s[high], s[low]
        low = low + 1
        high -= 1


def reverse_words_eff(str_in):
    s = list(str_in)
    start = 0
    while True:
        try:
            end = s.index(' ', start)
            reverse_word(s, start, end - 1)
            start = end + 1
        except ValueError:
            reverse_word(s, start, len(s) - 1)
            break
    s.reverse()
    s = "".join(s)
    return s


def main():
    str_input = "I love coding"
    print(reverse_words(str_input))
    print(reverse_words_eff(str_input))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
