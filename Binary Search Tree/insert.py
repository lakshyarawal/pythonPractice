""" Insert Operation in BSTs """


class Node:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None


def insert(root_n, val_in):
    if root_n is None:
        root_n = Node(val_in)
        return root_n
    elif root_n.key > val_in:
        root_n.left = insert(root_n.left, val_in)
    else:
        root_n.right = insert(root_n.right, val_in)
    return root_n


def insert_iter(root_n, val_in):
    if root_n.key == val_in:
        return root_n
    temp = Node(val_in)
    parent = None
    curr_node = root_n
    while curr_node:
        parent = curr_node
        if curr_node.key < val_in:
            curr_node = curr_node.right
        elif curr_node.key > val_in:
            curr_node = curr_node.left
        else:
            return root_n
    if parent is None:
        return temp
    if parent.key < val_in:
        parent.right = temp
    else:
        parent.left = temp
    return root_n


def main():
    root = Node(30)
    root.left = Node(20)
    root.right = Node(40)
    root.right.left = Node(35)
    root.right.right = Node(50)
    n_root = insert(root, 70)
    p_root = insert_iter(root, 70)


if __name__ == "__main__":
    main()
