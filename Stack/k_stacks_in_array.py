""" Class that implements K stacks in an array """


class KStacks:

    def __init__(self, cap, k):
        self.tops = [-1] * k
        self.arr = [0] * cap
        self.next = [-1] * cap
        self.free_top = 0
        for i in range(cap-1):
            self.next[i] = i+1
        self.capacity = cap

    def push(self, ele, stack):
        i = self.free_top
        self.free_top = self.next[i]
        self.arr[i] = ele
        self.next[i] = self.tops[stack]
        self.tops[stack] = i

    def pop(self, stack):
        i = self.tops[stack]
        self.tops[stack] = self.next[i]
        self.next[i] = self.free_top
        self.free_top = i
        return self.arr[i]


def main():
    k_obj = KStacks(6, 3)
    k_obj.push(100, 0)
    k_obj.push(200, 0)
    k_obj.push(300, 0)
    k_obj.push(400, 1)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
