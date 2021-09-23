"""Cloning a LinkedList with random pointers: """


class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
        self.random = None


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


""" One approach would be to create a hashmap of nodes and then create a new list based on their next and random
    Here: we introduce new nodes after existing nodes with same value, set the same random pointer and then extract"""


def cloning_list(l_list):
    n_list = LinkedList()
    if l_list.head is None:
        return
    if l_list.head.next is None:
        n_list.head = Node(l_list.head.data)
        return
    curr_node = l_list.head
    # Step 1 is to add dummy nodes that will have the same randoms, next and values
    while curr_node:
        next_node = curr_node.next
        curr_node.next = Node(curr_node.data)
        curr_node.next.next = next_node
        curr_node = next_node
    # Step 2 is to assign the same random values
    curr_node = l_list.head
    while curr_node and curr_node.next:
        if curr_node.random is None:
            curr_node.next.random = None
        else:
            curr_node.next.random = curr_node.random.next
        curr_node = curr_node.next.next
    # Step 3 is to extract these nodes from this list repairing the original connections
    curr_node = l_list.head
    n_list.head = curr_node.next
    while curr_node:
        next_node = curr_node.next.next
        if next_node is None:
            curr_node.next.next = None
        else:
            curr_node.next.next = next_node.next
        curr_node.next = next_node
        curr_node = next_node
    return n_list


def main():
    l_list = LinkedList()

    l_list.head = Node(10)
    second = Node(5)
    third = Node(20)
    fourth = Node(15)
    fifth = Node(20)

    l_list.head.next = second
    l_list.head.random = third
    second.next = third  # Link second node with the third node
    second.random = fourth
    third.next = fourth
    third.random = l_list.head
    fourth.next = fifth
    fourth.random = third
    fifth.random = fourth

    l_list2 = cloning_list(l_list)
    l_list2.print_list()
    l_list.print_list()


if __name__ == '__main__':
    # Start with the empty list
    main()
