""" Ceil Operation in BSTs """
from insert import Node


def ciel_iter(root_n, val_in):
    temp = None
    while root_n:
        if root_n.key == val_in:
            return root_n
        elif root_n.key > val_in:
            temp = root_n
            root_n = root_n.left
        if root_n.key < val_in:
            root_n = root_n.right
    return temp


def search_iter(root_n, val_in):
    while root_n:
        if root_n.key == val_in:
            print("Element Found")
            return
        elif root_n.key > val_in:
            root_n = root_n.left
        else:
            root_n = root_n.right
    print("Element Not Found")
    return


def main():
    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)
    root.right.left = Node(25)
    root.right.right = Node(50)
    n_node = ciel_iter(root, 27)
    print(n_node.key)


if __name__ == "__main__":
    main()
