""" Printing Nodes present at height K"""
from binary_tree_traversal_and_height import Node


def nodes_k(root_n, k):
    if root_n is None:
        return
    if k == 0:
        print(root_n.value, end=" ")
        return
    nodes_k(root_n.left_child, k-1)
    nodes_k(root_n.right_child, k-1)


def main():
    root = Node(10)
    root.left_child = Node(6)
    root.right_child = Node(8)
    root.right_child.right_child = Node(7)
    root.right_child.right_child.left_child = Node(11)
    root.right_child.right_child.right_child = Node(12)
    nodes_k(root, 3)


if __name__ == "__main__":
    main()
