""" Search Operation in BSTs """


class Node:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None


def search(root_n, val_in):
    if root_n is None:
        print("Element Not Found")
        return
    elif root_n.key == val_in:
        print("Element Found")
        return
    elif root_n.key > val_in:
        search(root_n.left, val_in)
    else:
        search(root_n.right, val_in)
    return


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
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.right.left = Node(40)
    root.right.right = Node(50)
    search(root, 50)
    search_iter(root, 50)


if __name__ == "__main__":
    main()
