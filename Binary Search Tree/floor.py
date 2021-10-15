""" Floor Operation in BSTs """
from insert import Node


def floor_iter(root_n, val_in):
    temp = None
    while root_n:
        if root_n.key == val_in:
            return root_n
        elif root_n.key > val_in:
            root_n = root_n.left
        if root_n.key < val_in:
            temp = root_n
            root_n = root_n.right
    return temp


def floor(root_n, val_in, curr):
    if root_n is None:
        return root_n
    if root_n.key < val_in:
        if curr < root_n.key:
            curr = root_n.key
            if root_n.right is None:
                return curr
            elif root_n.right.key > val_in:
                if root_n.right.left is None:
                    return curr
                return floor(root_n.right, val_in, curr)
            return floor(root_n.right, val_in, curr)
    if root_n.key > val_in:
        if root_n.left is None:
            return curr
        return floor(root_n.left, val_in, curr)
    if root_n.key == val_in:
        return root_n.key
    return curr


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
    n_node = floor_iter(root, 27)
    print(n_node.key)
    print(floor(root, 27, -1))


if __name__ == "__main__":
    main()
