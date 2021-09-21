""" To check if the given binary tree is balanced or not. balanced means that the difference in height of all sub
    trees is less than or equal to 1 """
from binary_tree_traversal_and_height import Node


def is_balanced(root_n):
    if root_n is None:
        return 0
    lh = is_balanced(root_n.left_child)
    if lh == -1:
        return -1
    rh = is_balanced(root_n.right_child)
    if rh == -1:
        return -1
    if abs(lh-rh) > 1:
        return -1
    else:
        return max(lh, rh) + 1


def main():
    root = Node(30)
    root.left_child = Node(40)
    root.right_child = Node(80)
    root.right_child.left_child = Node(5)
    root.left_child.left_child = Node(50)
    root.left_child.right_child = Node(70)
    root.left_child.right_child.left_child = Node(20)
    root.left_child.right_child.right_child = Node(10)
    print(is_balanced(root))


if __name__ == "__main__":
    main()
