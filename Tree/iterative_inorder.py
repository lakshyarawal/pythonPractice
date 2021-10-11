""" Doing inorder traversal of binary tree using iterative methods """
from binary_tree_traversal_and_height import Node
from collections import deque


def iter_in(root_n):
    if root_n is None:
        print("")
        return
    curr_node = root_n
    q1 = deque()
    while len(q1) > 0 or curr_node:
        while curr_node:
            q1.append(curr_node)
            curr_node = curr_node.left_child
        curr_node = q1.pop()
        print(curr_node.value, end=" ")
        curr_node = curr_node.right_child


def main():
    root = Node(10)
    root.left_child = Node(20)
    root.right_child = Node(30)
    root.left_child.right_child = Node(50)
    root.left_child.left_child = Node(40)
    root.right_child.left_child = Node(60)
    iter_in(root)


if __name__ == "__main__":
    main()
