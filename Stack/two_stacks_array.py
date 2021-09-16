""" Balanced Parentheses using Stack Data Structure """


class TwoStacks:

    def __init__(self, cap):
        self.arr = [0] * cap
        self.top1 = -1
        self.top2 = cap
        self.capacity = cap

    def push1(self, ele):
        if self.top1 < self.top2-1:
            self.top1 += 1
            self.arr[self.top1] = ele
        else:
            print("Array is full")
            return

    def push2(self, ele):
        if self.top1 < self.top2-1:
            self.top2 -= 1
            self.arr[self.top2] = ele
        else:
            print("Array is full")
            return

    def pop1(self):
        if self.top1 >= 0:
            ele = self.arr[self.top1]
            self.arr[self.top1] = 0
            self.top1 -= 1
            return ele
        else:
            print("Array is empty for 1 stack")
            return

    def pop2(self):
        if self.top2 < self.capacity:
            ele = self.arr[self.top2]
            self.arr[self.top2] = 0
            self.top2 += 1
            return ele
        else:
            print("Array is empty for 2 stack")
            return


def main():
    str_input = "((())"


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
