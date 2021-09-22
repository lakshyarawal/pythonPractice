""" Finding the maximum width of the tree"""
from binary_tree_traversal_and_height import Node
from collections import deque


def max_width(root_n):
    if root_n is None:
        return 0
    else:
        max_wid = 0
        q1 = deque()
        q1.append(root_n)

    while len(q1) > 0:
        curr_size = len(q1)
        max_wid = max(max_wid, curr_size)
        i = 0

        while i < curr_size:
            curr = q1.popleft()
            print(curr.value, end=" ")
            if curr.left_child is not None:
                q1.append(curr.left_child)
            if curr.right_child is not None:
                q1.append(curr.right_child)
            i += 1
        print("")

    return max_wid


def main():
    root = Node(10)
    root.left_child = Node(20)
    root.right_child = Node(30)
    root.right_child.left_child = Node(50)
    root.right_child.right_child = Node(60)
    root.left_child.left_child = Node(40)
    root.left_child.left_child.left_child = Node(80)
    print(max_width(root))


if __name__ == "__main__":
    main()