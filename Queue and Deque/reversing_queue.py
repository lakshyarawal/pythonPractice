""" Implementing a stack using queue """
from collections import deque


def reverse_q(q1):
    q2 = deque()
    while len(q1) > 0:
        temp = q1.pop()
        q2.append(temp)
    return q2


def main():
    q_in = deque()
    q_in.append(1)
    q_in.append(22)
    q_in.append(33)
    q_in.append(44)
    print(reverse_q(q_in))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
