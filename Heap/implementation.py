""" Binary Heap Data Structure Implementation in Python """


class Heap:
    def __init__(self, cap):
        self.capacity = cap
        self.arr = [0 for _ in range(cap)]
        self.size = 0

    def insert(self, val):
        if self.capacity > self.size:
            self.size += 1
            self.arr[self.size - 1] = val
            temp = self.size-1
            while self.arr[(temp-1)//2] > self.arr[temp] and temp != 0:
                self.arr[temp], self.arr[(temp-1)//2] = self.arr[(temp-1)//2], self.arr[temp]
                temp = (temp-1)//2
        else:
            print("Heap is Full")
            return


def main():
    h = Heap(10)
    h.insert(10)
    h.insert(50)
    h.insert(5)
    print(h.arr)


if __name__ == "__main__":
    main()
