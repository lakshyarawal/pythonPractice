""" Doing pre order traversal of binary tree using iterative methods """
from binary_tree_traversal_and_height import Node
from collections import deque


def iter_pre_un(root_n):
    if root_n is None:
        return
    q1 = deque()
    q1.append(root_n)
    while len(q1) > 0:
        curr_node = q1.pop()
        print(curr_node.value, end=" ")
        if curr_node.right_child is not None:
            q1.append(curr_node.right_child)
        if curr_node.left_child is not None:
            q1.append(curr_node.left_child)


def iter_pre(root_n):
    if root_n is None:
        return
    curr_node = root_n
    q1 = deque()
    while len(q1) > 0 or curr_node:
        while curr_node:
            print(curr_node.value, end=" ")
            if curr_node.right_child is not None:
                q1.append(curr_node.right_child)
            curr_node = curr_node.left_child
        if len(q1) > 0:
            curr_node = q1.pop()


def main():
    root = Node(10)
    root.left_child = Node(20)
    root.right_child = Node(30)
    root.left_child.right_child = Node(50)
    root.left_child.left_child = Node(40)
    root.right_child.left_child = Node(60)
    iter_pre(root)


if __name__ == "__main__":
    main()
