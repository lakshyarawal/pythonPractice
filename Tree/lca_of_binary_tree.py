""" LCA: Lowest Common Ancestor of two values in a binary tree """
from binary_tree_traversal_and_height import Node
from collections import deque


def find_path(root_n, path_a, n):
    if root_n is None:
        return False
    path_a.append(root_n.value)
    if root_n.value == n:
        return True
    if find_path(root_n.left_child, path_a, n) or find_path(root_n.right_child, path_a, n):
        return True
    path_a.pop()
    return False


def lca_bin(root_n, n1, n2):
    if root_n is None:
        return False
    path_1 = deque()
    path_2 = deque()
    if find_path(root_n, path_1, n1) is False or find_path(root_n, path_2, n2) is False:
        return False
    i = 0
    print(path_1)
    print(path_2)
    while i < len(path_2) and i < len(path_1):
        if path_2[i+1] != path_1[i+1]:
            return path_1[i]
        i += 1
    return None


""" The above approach does 4 traversal of the tree and we can improve on this"""


def lca_eff(root_n, n1, n2):
    if root_n is None:
        return None
    if root_n.value == n1 or root_n.value == n2:
        return root_n.value
    lca1 = lca_eff(root_n.left_child, n1, n2)
    lca2 = lca_eff(root_n.right_child, n1, n2)
    if lca1 is not None and lca2 is not None:
        return root_n.value
    if lca1 is None:
        return lca2
    else:
        return lca1


def main():
    root = Node(10)
    root.left_child = Node(20)
    root.right_child = Node(30)
    root.right_child.left_child = Node(40)
    root.right_child.right_child = Node(50)
    root.right_child.left_child.left_child = Node(60)
    root.right_child.right_child.left_child = Node(70)
    root.right_child.right_child.right_child = Node(80)
    print(lca_bin(root, 60, 70))
    print(lca_eff(root, 60, 70))


if __name__ == "__main__":
    main()
