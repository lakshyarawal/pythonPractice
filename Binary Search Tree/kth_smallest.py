"""Finding the Kth Smallest Element"""


class Node:
    def __init__(self, val, count):
        self.key = val
        self.left = None
        self.right = None
        self.count = count


def kth_smallest_eff(root_n, k):
    if root_n:
        if root_n.count == k:
            print(root_n.key)
            return
        elif root_n.count > k:
            kth_smallest_eff(root_n.left, k)
        else:
            kth_smallest_eff(root_n.right, k)
    return


def kth_smallest(root_n, k):
    if root_n:
        kth_smallest(root_n.left, k)
        kth_smallest.count += 1
        if kth_smallest.count == k:
            print(root_n.key)
            return
        kth_smallest(root_n.right, k)
    return


kth_smallest.count = 0


def main():
    root = Node(50, 4)
    root.left = Node(20, 2)
    root.right = Node(100, 8)
    root.left.left = Node(10, 1)
    root.left.right = Node(40, 3)
    root.right.left = Node(70, 6)
    root.right.right = Node(120, 9)
    root.right.left.left = Node(60, 5)
    root.right.left.right = Node(8, 7)
    kth_smallest(root, 3)
    kth_smallest_eff(root, 3)


if __name__ == "__main__":
    main()
