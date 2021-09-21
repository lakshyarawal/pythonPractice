""" Maximum value in a binary tree"""
from binary_tree_traversal_and_height import Node
from collections import deque


def max_val(root_n):
    max_bin = -1
    q1 = deque()
    q1.append(root_n)
    while len(q1) > 0:
        curr = q1.popleft()
        max_bin = max(curr.value, max_bin)
        if curr.left_child is not None:
            q1.append(curr.left_child)
        if curr.right_child is not None:
            q1.append(curr.right_child)
    return max_bin


def max_val_rec(root_n):
    if root_n is None:
        return -1
    else:
        return max(max_val_rec(root_n.left_child), max_val_rec(root_n.right_child), root_n.value)


def main():
    root = Node(10)
    root.left_child = Node(20)
    root.right_child = Node(30)
    root.right_child.right_child = Node(60)
    root.left_child.left_child = Node(40)
    root.left_child.right_child = Node(50)
    root.right_child.right_child.left_child = Node(70)
    root.right_child.right_child.right_child = Node(80)
    print(max_val_rec(root))


if __name__ == "__main__":
    main()

