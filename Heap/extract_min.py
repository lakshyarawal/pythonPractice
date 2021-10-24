"""Heapify Function in Binary Heap Data Structure in Python """


class Heap:
    def __init__(self, cap):
        self.capacity = cap
        self.arr = [0 for _ in range(cap)]
        self.size = 0

    def insert(self, val):
        if self.capacity > self.size:
            self.size += 1
            self.arr[self.size - 1] = val
        else:
            print("Heap is Full")
            return

    def heapify(self, position):
        left = 2*position + 1
        right = 2*position + 2
        if left >= self.size or right >= self.size:
            return
        if self.arr[position] > self.arr[left] or self.arr[position] > self.arr[right]:
            if self.arr[left] < self.arr[right]:
                self.arr[position], self.arr[left] = self.arr[left], self.arr[position]
                self.heapify(left)
            else:
                self.arr[position], self.arr[right] = self.arr[right], self.arr[position]
                self.heapify(right)
        return

    def extract_min(self):
        self.arr[0], self.arr[self.size-1] = self.arr[self.size-1], self.arr[0]
        self.arr[self.size-1] = 0
        self.heapify(0)
        return


def main():
    h = Heap(10)
    h.insert(40)
    h.insert(20)
    h.insert(30)
    h.insert(35)
    h.insert(25)
    h.insert(80)
    h.insert(32)
    h.insert(100)
    h.insert(70)
    h.insert(60)
    print(h.arr)
    h.heapify(0)
    print(h.arr)
    h.extract_min()
    print(h.arr)


if __name__ == "__main__":
    main()
