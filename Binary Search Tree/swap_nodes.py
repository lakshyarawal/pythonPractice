""" We are give a tree that can be converted into a BST by swapping two nodes. We have to find and swap them """


class Node:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None


def swap_nodes(root_n):
    if root_n is None:
        return
    swap_nodes(root_n.left)
    if root_n.key < swap_nodes.prev.key:
        if swap_nodes.node1 is None:
            swap_nodes.node1 = swap_nodes.prev
        swap_nodes.node2 = root_n
    swap_nodes.prev = root_n
    swap_nodes(root_n.right)


swap_nodes.prev = Node(-1000)
swap_nodes.node1 = None
swap_nodes.node2 = None


def main():
    root = Node(20)
    root.left = Node(60)
    root.right = Node(80)
    root.left.left = Node(4)
    root.left.right = Node(10)
    root.right.left = Node(8)
    root.right.right = Node(100)
    swap_nodes(root)
    print(swap_nodes.node1.key)
    print(swap_nodes.node2.key)


if __name__ == "__main__":
    main()
