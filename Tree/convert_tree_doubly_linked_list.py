""" Converting a tree into a doubly linked list """


class Node(object):

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


def tree_to_list(root_n):
    if root_n is None:
        return root_n

    if root_n.left:
        left = tree_to_list(root_n.left)
        while left.right:
            left = left.right
        left.right = root_n
        root_n.left = left

    if root_n.right:

        right = tree_to_list(root_n.right)
        while right.left:
            right = right.left
        root_n.right = right

    return root_n


def main_tree_to_list(root_in):
    if root_in is None:
        return root_in

    root_in = tree_to_list(root_in)

    while root_in.left:
        root_in = root_in.left

    return root_in


def print_list(head_in):
    if head_in is None:
        return
    while head_in:
        print(head_in.data, end=" ")
        head_in = head_in.right


# Driver Code
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)

    head = main_tree_to_list(root)
    print_list(head)
