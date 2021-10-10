""" Serialization and Deserialization of a binary tree: Given the pointer to the root node of the tree we have to
    convert it into a string such that we can reconstruct the tree from this string """
from binary_tree_traversal_and_height import Node
from collections import deque


def serialize(root_n, arr_in):
    if root_n.left_child is not None:
        arr_in.append(root_n.left_child.value)
        serialize.q1.append(root_n.left_child)
    else:
        arr_in.append(" ")
    if root_n.right_child is not None:
        arr_in.append(root_n.right_child.value)
        serialize.q1.append(root_n.right_child)
    else:
        arr_in.append(" ")
    if len(serialize.q1) > 0:
        arr_in = serialize(serialize.q1.popleft(), arr_in)
    return arr_in


serialize.q1 = deque()


def deserialize(arr_in):
    root_n = Node(arr_in[0])
    i = 1
    deserialize.q1.append(root_n)
    print(root_n.value)
    while i < len(arr_in):
        curr_node = deserialize.q1.popleft()
        if arr_in[i] == " ":
            curr_node.left_child = None
        else:
            t_l = Node(arr_in[i])
            curr_node.left_child = t_l
            deserialize.q1.append(t_l)
        i += 1
        if arr_in[i] == " ":
            curr_node.right_child = None
        else:
            t_r = Node(arr_in[i])
            curr_node.right_child = t_r
            deserialize.q1.append(t_r)
        i += 1
    return root_n


deserialize.q1 = deque()

def main():
    root = Node(10)
    root.left_child = Node(50)
    root.right_child = Node(60)
    root.left_child.right_child = Node(20)
    root.left_child.left_child = Node(70)
    root.right_child.left_child = Node(8)
    arr = [root.value]
    print(serialize(root, arr))
    deserialize(serialize(root, arr))


if __name__ == "__main__":
    main()

