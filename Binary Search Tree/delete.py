""" Delete Operation in BSTs """
from insert import Node


def delete(root_n, val_in):
    if root_n is None:
        print("Element Not Found")
        return root_n
    elif root_n.key < val_in:
        root_n.right = delete(root_n.right, val_in)
    elif root_n.key > val_in:
        root_n.left = delete(root_n.left, val_in)
    else:
        if root_n.left is None:
            return root_n.right
        elif root_n.right is None:
            return root_n.left
        else:
            temp = root_n.right
            while temp and temp.left:
                temp = temp.left
            root_n.key = temp.key
            root_n.right = delete(root_n.right, temp.key)
    return root_n


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
    delete(root, 50)
    search_iter(root, 50)


if __name__ == "__main__":
    main()
