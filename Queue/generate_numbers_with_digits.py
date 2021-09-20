""" Generate Numbers with digits"""
from collections import deque
from Mathematics import factorial


def generate_digits(s1, n):
    q2 = deque()
    set_len = len(s1)
    j = 0
    q2.append(str(s1[j]))
    j = (j + 1) % set_len
    q2.append(str(s1[j]))
    j = (j + 1) % set_len
    for i in range(n):
        curr = q2.popleft()
        print(curr, end=" ")
        q2.append(curr + str(s1[j]))
        j = (j + 1) % set_len
        q2.append(curr + str(s1[j]))
        j = (j + 1) % set_len


def main():
    arr = [5, 6]
    generate_digits(arr, 10)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()