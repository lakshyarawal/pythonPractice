"""Decrease a key in of a Binary Heap """


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

    def leftChild(self, pos):
        return 2 * pos

        # Function to return the position of
        # the right child for the node currently
        # at pos

    def rightChild(self, pos):
        return (2 * pos) + 1

        # Function that returns true if the passed
        # node is a leaf node

    def isLeaf(self, pos):
        if pos >= (self.size // 2) and pos <= self.size:
            return True
        return False

    def swap(self, fpos, spos):
        self.arr[fpos], self.arr[spos] = self.arr[spos], self.arr[fpos]

    def heapify(self, pos):
        # If the node is a non-leaf node and greater
        # than any of its child
        if not self.isLeaf(pos):
            if (self.arr[pos] > self.arr[self.leftChild(pos)] or
                    self.arr[pos] > self.arr[self.rightChild(pos)]):

                # Swap with the left child and heapify
                # the left child
                if self.arr[self.leftChild(pos)] < self.arr[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.heapify(self.leftChild(pos))

                # Swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.heapify(self.rightChild(pos))

    def decrease_key(self, new_val, index):
        self.arr[index] = new_val
        temp = (index-1)//2
        while index != 0 and self.arr[index] < self.arr[temp]:
            self.arr[index], self.arr[temp] = self.arr[temp], self.arr[index]
            index = temp
            temp = (temp-1)//2
        return

    def extract_min(self):
        if self.size == 0:
            return
        if self.size == 1:
            a = self.arr[0]
            self.arr[0] = 0
            self.size -= 1
            return a
        a = self.arr[0]
        self.arr[0], self.arr[self.size-1] = self.arr[self.size-1], self.arr[0]
        self.arr[self.size-1] = 0
        self.size -= 1
        self.heapify(0)
        return a

    def delete_key(self, index):
        self.decrease_key(-1000, index)
        self.extract_min()
        return


def build_heap(arr):
    h = Heap(len(arr))
    for i in range(len(arr)):
        h.insert(arr[i])
    print(h.arr)
    for i in range((len(arr)-2)//2, -1, -1):
        h.heapify(i)
    return h.arr


def main():
    h = Heap(6)
    h.insert(10)
    h.insert(20)
    h.insert(40)
    h.insert(80)
    h.insert(100)
    h.insert(70)
    h.heapify(0)
    print(h.arr)
    h.decrease_key(5, 3)
    print(h.arr)
    h.delete_key(3)
    print(h.arr)
    n_arr = [10, 5, 20, 2, 4, 8]
    print("New heap: ", build_heap(n_arr))


if __name__ == "__main__":
    main()
