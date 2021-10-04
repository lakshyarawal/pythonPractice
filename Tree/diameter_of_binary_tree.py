""" Diameter of a Binary Tree - No. of Nodes in the longest path between two leaf nodes """
from binary_tree_traversal_and_height import Node

""" In this solution we compute the diameter at each node and then compare it with it's left and right child """


def height_tree(root_n):
    if root_n is None:
        return 0
    else:
        return 1 + max(height_tree(root_n.right_child), height_tree(root_n.left_child))


def diameter_tree(root_n):
    if root_n is None:
        return 0
    d1 = 1 + height_tree(root_n.left_child) + height_tree(root_n.right_child)
    d2 = diameter_tree(root_n.left_child)
    d3 = diameter_tree(root_n.right_child)
    return max(d1, d2, d3)


""" Efficient Solution: We compute the height at each node and then store it in a hash map """


def diameter_tree_eff(root_n, h_map):
    if root_n is None:
        return 0
    h_map[root_n] = 1 + height_tree(root_n.left_child) + height_tree(root_n.right_child)
    diameter_tree_eff(root_n.left_child, h_map)
    diameter_tree_eff(root_n.right_child, h_map)


""" Another approach would be to modify the height function and store the max height as it is being calculated """


def diameter_tree_eff_h(root_n):
    if root_n is None:
        return 0
    lh = height_tree(root_n.left_child)
    rh = height_tree(root_n.right_child)
    diameter_tree_eff_h.res = max(diameter_tree_eff_h.res, lh+rh+1)
    return 1 + max(lh, rh)


diameter_tree_eff_h.res = 0


def main():
    root = Node(10)
    root.left_child = Node(20)
    root.right_child = Node(30)
    root.right_child.left_child = Node(40)
    root.right_child.right_child = Node(50)
    root.right_child.left_child.left_child = Node(60)
    print(diameter_tree(root))
    he_map = {}
    diameter_tree_eff(root, he_map)
    print(max(he_map.values()))
    diameter_tree_eff_h(root)
    print(diameter_tree_eff_h.res)


if __name__ == "__main__":
    main()
