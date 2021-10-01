""" To print the tree in a spiral form """
from binary_tree_traversal_and_height import Node
from collections import deque


def print_spiral(root_n):
    q1 = deque()
    q2 = deque()
    q1.append(root_n)
    while len(q1):
        while len(q1):
            curr = q1.pop()
            print(curr.value, end=" ")
            if curr.left_child is not None:
                q2.append(curr.left_child)
            if curr.right_child is not None:
                q2.append(curr.right_child)
        print("")
        while len(q2):
            curr = q2.pop()
            print(curr.value, end=" ")
            if curr.right_child is not None:
                q1.append(curr.right_child)
            if curr.left_child is not None:
                q1.append(curr.left_child)
        print("")


def main():
    root = Node(10)
    root.left_child = Node(20)
    root.right_child = Node(30)
    root.right_child.left_child = Node(40)
    root.right_child.right_child = Node(50)
    root.right_child.left_child.right_child = Node(70)
    root.right_child.left_child.left_child = Node(60)
    root.right_child.right_child.right_child = Node(80)
    print_spiral(root)


if __name__ == "__main__":
    main()
