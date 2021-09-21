""" Size of binary tree"""
from binary_tree_traversal_and_height import Node
from collections import deque


def size_of_t(root_n):
    count_bin = 0
    q1 = deque()
    q1.append(root_n)
    while len(q1) > 0:
        curr = q1.popleft()
        count_bin += 1
        if curr.left_child is not None:
            q1.append(curr.left_child)
        if curr.right_child is not None:
            q1.append(curr.right_child)
    return count_bin


def size_of_t_rec(root_n):
    if root_n is None:
        return 0
    else:
        return size_of_t_rec(root_n.left_child) + size_of_t_rec(root_n.right_child) + 1


def main():
    root = Node(10)
    root.left_child = Node(20)
    root.right_child = Node(30)
    root.right_child.right_child = Node(60)
    root.left_child.left_child = Node(40)
    root.left_child.right_child = Node(50)
    root.right_child.right_child.left_child = Node(70)
    root.right_child.right_child.right_child = Node(80)
    print(size_of_t_rec(root))


if __name__ == "__main__":
    main()

