""" We need to construct the binary tree using the pre order and in order traversals of the tree """
from binary_tree_traversal_and_height import Node


def construct_tree(in_ord, pr_ord, i_s, i_e):
    if i_s > i_e:
        return None

    # Assign Root as the first element in the pre-order traversal
    root = Node(pr_ord[construct_tree.pre_index])
    construct_tree.pre_index += 1
    # Find where root is present in the in-order traversal and then divide the array into
    # left and right child and then repeat the process
    if i_s == i_e:
        return root
    cut = search(in_ord, i_s, i_e, root.value)
    root.left_child = construct_tree(in_ord, pr_ord, i_s, cut-1)
    root.right_child = construct_tree(in_ord, pr_ord, cut+1, i_e)
    return root


def search(arr, start, end, value):
    for i in range(start, end + 1):
        if arr[i] == value:
            return i


def print_inorder(node):
    if node is None:
        return
    # first recur on left child
    print_inorder(node.left_child)

    # then print the data of node
    print(node.value, end="->")

    # now recur on right child
    print_inorder(node.right_child)


construct_tree.pre_index = 0


def main():
    in_trv = [20, 10, 40, 30, 50]
    pre_trv = [10, 20, 30, 40, 50]
    r = construct_tree(in_trv, pre_trv, 0, len(in_trv)-1)
    print_inorder(r)


if __name__ == "__main__":
    main()
