"""Finding sum of all nodes that lie in a vertical line """


class Node:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None


def vertical_sum(root_n, curr_sum, sum_map):
    if root_n is None:
        return
    vertical_sum(root_n.left, curr_sum-1, sum_map)
    if curr_sum in sum_map.keys():
        sum_map[curr_sum] += root_n.key
    else:
        sum_map[curr_sum] = root_n.key
    vertical_sum(root_n.right, curr_sum+1, sum_map)
    return sum_map.values()


def main():
    root = Node(10)
    root.left = Node(15)
    root.left.left = Node(35)
    root.left.right = Node(20)
    root.right = Node(25)
    root.left.left.left = Node(40)
    root.left.right.right = Node(75)
    root.left.right.right.right = Node(80)
    print(vertical_sum(root, 0, {}))


if __name__ == "__main__":
    main()
