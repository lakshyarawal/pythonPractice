""" Count Nodes present in a complete binary tree """
from binary_tree_traversal_and_height import Node


def count_nodes(root_n):
    if root_n is None:
        return 0
    temp = root_n
    l_count = 0
    r_count = 0
    while temp:
        l_count += 1
        temp = temp.left_child
    temp = root_n
    while temp:
        r_count += 1
        temp = temp.right_child
    if l_count == r_count:
        return pow(2, l_count) - 1
    else:
        return 1 + count_nodes(root_n.left_child) + count_nodes(root_n.right_child)


def main():
    root = Node(10)
    root.left_child = Node(50)
    root.right_child = Node(60)
    root.left_child.right_child = Node(20)
    root.left_child.left_child = Node(70)
    root.right_child.left_child = Node(8)
    print(count_nodes(root))


if __name__ == "__main__":
    main()

