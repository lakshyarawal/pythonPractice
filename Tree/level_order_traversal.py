""" Level Order Traversal: Using queue data structure"""
from binary_tree_traversal_and_height import Node
from collections import deque


def level_oder_trv(root_n):
    q1 = deque()
    if root_n is not None:
        q1.append(root_n)
    while len(q1) > 0:
        curr_size = len(q1)
        i = 0
        while i < curr_size:
            cur_node = q1.popleft()
            print(cur_node.value, end=" ")
            if cur_node.left_child is not None:
                q1.append(cur_node.left_child)
            if cur_node.right_child is not None:
                q1.append(cur_node.right_child)
            i += 1
        print("")


def main():
    root = Node(10)
    root.left_child = Node(20)
    root.right_child = Node(30)
    root.right_child.right_child = Node(60)
    root.left_child.left_child = Node(40)
    root.left_child.right_child = Node(50)
    root.right_child.right_child.left_child = Node(70)
    root.right_child.right_child.right_child = Node(80)
    level_oder_trv(root)


if __name__ == "__main__":
    main()

