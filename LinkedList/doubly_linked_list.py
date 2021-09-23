""" Doubly LinkedList Implementation: """


class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
        self.prev = None  # Initialize prev as null


class DoubleLinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("")

    def reverse(self):
        temp = None
        current = self.head

        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        if temp is not None:
            self.head = temp.prev


def insert_begin(d_list, new_node):
    if d_list.head is None:
        d_list.head = new_node
        return
    new_node.next = d_list.head
    d_list.head.prev = new_node
    d_list.head = new_node


def insert_end(d_list, new_node):
    if d_list.head is None:
        d_list.head = new_node
        return
    temp = d_list.head
    while temp:
        if temp.next is None:
            temp.next = new_node
            new_node.prev = temp
            return
        temp = temp.next


def delete_head(d_list):
    if d_list.head is None:
        return
    if d_list.head.next is None:
        d_list.head = None
        return
    d_list.head = d_list.head.next
    d_list.head.prev = None


def delete_last(d_list):
    if d_list.head is None:
        return
    if d_list.head.next is None:
        d_list.head = None
        return
    temp = d_list.head
    while temp:
        if temp.next is None:
            temp.prev.next = None
            return
        temp = temp.next


def main():
    d_list = DoubleLinkedList()

    d_list.head = Node(10)
    second = Node(20)
    third = Node(30)

    d_list.head.next = second
    second.prev = d_list.head  # Link first node with second
    second.next = third  # Link second node with the third node
    third.prev = second
    d_list.print_list()

    insert_begin(d_list, Node(22))
    d_list.print_list()

    insert_end(d_list, Node(44))
    d_list.print_list()

    d_list.reverse()
    d_list.print_list()

    delete_head(d_list)
    d_list.print_list()

    delete_last(d_list)
    d_list.print_list()


if __name__ == '__main__':
    # Start with the empty list
    main()
