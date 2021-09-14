"""Reversing the elements of the given linked list is groups of k. so if list is 10, 20, 30, 40, 50, 60 and k = 3
    then the output would be: 30, 20, 10, 60, 50, 40"""


class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("")


def reverse_list_group_rec(l_list_head, k):
    if l_list_head is None or l_list_head.next is None:
        return
    temp = l_list_head
    i = 0
    next_node = None
    prev_node = None

    while temp and i < k:
        next_node = temp.next
        temp.next = prev_node
        prev_node = temp
        temp = next_node
        i += 1
    if next_node:
        res_head = reverse_list_group(next_node, k)
        l_list_head.next = res_head
    return prev_node


""" Iterative Solution: """


def reverse_list_group(l_list_head, k):
    if l_list_head is None or l_list_head.next is None:
        return
    prev_first = None
    cur_node = l_list_head
    bool_pass = True
    while cur_node:
        i = 0
        prev_node = None
        first = cur_node
        while i < k:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
            i += 1
        if bool_pass:
            l_list_head = prev_node
            bool_pass = False
        else:
            prev_first.next = prev_node
        prev_first = first
    return l_list_head


def main():
    l_list = LinkedList()

    l_list.head = Node(10)
    second = Node(20)
    third = Node(30)
    fourth = Node(40)
    fifth = Node(50)
    sixth = Node(60)

    l_list.head.next = second
    second.next = third  # Link second node with the third node
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth

    l_list.print_list()
    l_list.head = reverse_list_group(l_list.head, 3)
    l_list.print_list()


if __name__ == '__main__':
    # Start with the empty list
    main()
