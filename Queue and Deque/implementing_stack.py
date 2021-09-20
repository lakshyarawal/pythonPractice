""" Implementing a stack using queue """
from collections import deque


class StackQ:
    def __init__(self):
        self.q = deque()
        self.size = 0

    def top(self):
        return self.q[0]

    def push(self, val):
        self.size += 1
        self.q.append(val)

    def pop(self):
        return self.q.pop()

    def size_st(self):
        return self.size


def main():
    st = StackQ()
    st.push(10)
    st.push(20)
    st.push(30)
    print(st.size_st())
    st.pop()
    print(st.top())


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
