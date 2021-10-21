"""Finding if a pair in the BST has the given number as their sum """


class Node:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None


def pair_sum(root_n, total_sum, sum_arr):
    if root_n is None:
        return
    pair_sum(root_n.left, total_sum, sum_arr)
    i = len(sum_arr) - 1
    while i > 0:
        if root_n.key in sum_arr:
            print(root_n.key, total_sum - root_n.key)
            return
        i -= 1
    sum_arr.add(total_sum - root_n.key)
    pair_sum(root_n.right, total_sum, sum_arr)


def main():
    root = Node(10)
    root.left = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(9)
    root.right = Node(20)
    root.right.left = Node(11)
    root.right.right = Node(30)
    root.right.right.left = Node(25)
    pair_sum(root, 33, set())


if __name__ == "__main__":
    main()
