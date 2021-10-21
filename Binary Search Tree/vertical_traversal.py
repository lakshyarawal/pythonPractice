"""Traversing and printing all nodes present in a vertical line """
from collections import deque
from sortedcollections import SortedDict


class Node:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None


def vertical_traversal(root_n, sum_map):
    q1 = deque()
    if root_n is not None:
        q1.append([root_n, 0])
    while len(q1) > 0:
        curr_size = len(q1)
        i = 0
        while i < curr_size:
            cur_node, j = q1.popleft()
            if j in sum_map.keys():
                sum_map[j].append(cur_node.key)
            else:
                sum_map[j] = [cur_node.key]
            if cur_node.left is not None:
                q1.append([cur_node.left, j-1])
            if cur_node.right is not None:
                q1.append([cur_node.right, j+1])
            i += 1
    return sum_map


def main():
    root = Node(10)
    root.left = Node(15)
    root.left.left = Node(35)
    root.left.right = Node(20)
    root.right = Node(25)
    root.left.left.left = Node(40)
    root.left.right.right = Node(75)
    root.left.right.right.right = Node(80)
    a = vertical_traversal(root, SortedDict())
    for i in a.values():
        print(i)


if __name__ == "__main__":
    main()
