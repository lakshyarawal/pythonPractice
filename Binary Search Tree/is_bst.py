"""Given a tree we have to find if this is a binary search tree"""


class Node:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None


def is_bst(root_n, low_r, high_r):
    if root_n:
        return high_r > root_n.key > low_r \
               and is_bst(root_n.left, low_r, root_n.key) \
               and is_bst(root_n.right, root_n.key, high_r)
    else:
        return True


is_bst.bool_val = True


def is_bst_order(root_n):
    if root_n is None:
        return True
    if is_bst_order(root_n.left) is False:
        return False
    if root_n.key <= is_bst_order.prev:
        return False
    is_bst_order.prev = root_n.key
    return is_bst_order(root_n.right)


is_bst_order.prev = -1000


def main():
    root = Node(50)
    root.left = Node(20)
    root.right = Node(100)
    root.left.left = Node(10)
    root.left.right = Node(40)
    root.right.left = Node(70)
    root.right.right = Node(120)
    root.right.left.left = Node(60)
    root.right.left.right = Node(80)
    print(is_bst(root, -1000, 1000))
    print(is_bst_order(root))


if __name__ == "__main__":
    main()
