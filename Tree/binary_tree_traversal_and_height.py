""" Traversing a Binary Tree: There are two ways to do this, Depth First and Breadth First. In Breadth First we
    traverse from left to right on each level. In Depth First we have 3 common options: In Order (Left -> Root -> Right)
    , Post Order (Left -> Right -> Root) and Pre Order (Root -> Left -> Right)"""


class Node:
    def __init__(self, val):
        self.value = val
        self.left_child = None
        self.right_child = None


def inorder_trv(root_n):
    if root_n is not None:
        inorder_trv(root_n.left_child)
        print(root_n.value, end=" ")
        inorder_trv(root_n.right_child)


def preorder_trv(root_n):
    if root_n is not None:
        print(root_n.value, end=" ")
        preorder_trv(root_n.left_child)
        preorder_trv(root_n.right_child)


def postorder_trv(root_n):
    if root_n is not None:
        postorder_trv(root_n.left_child)
        postorder_trv(root_n.right_child)
        print(root_n.value, end=" ")


def height_tree(root_n):
    if root_n is not None:
        height_sub = max(height_tree(root_n.left_child), height_tree(root_n.right_child))
        return height_sub + 1
    return 0


def main():
    root = Node(10)
    root.left_child = Node(20)
    root.right_child = Node(30)
    root.right_child.left_child = Node(40)
    root.right_child.right_child = Node(50)
    inorder_trv(root)
    print("")
    preorder_trv(root)
    print("")
    postorder_trv(root)
    print("")
    print(height_tree(root))


if __name__ == "__main__":
    main()
