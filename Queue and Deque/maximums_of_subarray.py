""" Finding the maximum sub array  """
from collections import deque


def max_subs(ar_in, k):
    q2 = deque()
    q2.append(0)
    for z in range(1, k):
        if ar_in[z] < ar_in[q2[0]]:
            q2.append(z)
        else:
            while len(q2) > 0:
                q2.pop()
            q2.appendleft(z)
    for i in range(k, len(ar_in)):
        print(ar_in[q2[0]])
        while len(q2) > 0 and ar_in[q2[0]] <= i-k:
            q2.pop()
        if ar_in[i] < ar_in[q2[0]]:
            q2.append(i)
        else:
            while len(q2) > 0:
                q2.pop()
            q2.appendleft(i)
    print(ar_in[q2[0]])


def main():
    arr_in = [10, 8, 5, 12, 15, 7, 6]
    k = 3
    max_subs(arr_in, k)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
