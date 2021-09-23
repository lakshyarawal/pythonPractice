""" Circular LinkedList: """


class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


class CircularLinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                print("")
                break


""" To insert at begin and end in O(1) time we add node next to head and then swap the data with the head. Then mark
    the new head accordingly"""


def insert_begin(c_list, new_node):
    if c_list.head is None:
        c_list.head = new_node
        new_node.next = new_node
        return
    temp = c_list.head
    new_node.next = temp
    while temp:
        if temp.next == c_list.head:
            temp.next = new_node
            c_list.head = new_node
            return
        temp = temp.next


def insert_end(c_list, new_node):
    if c_list.head is None:
        c_list.head = new_node
        new_node.next = new_node
        return
    temp = c_list.head
    new_node.next = temp
    while temp:
        if temp.next == c_list.head:
            temp.next = new_node
            new_node.next = c_list.head
            return
        temp = temp.next


def delete_head(c_list):
    if c_list.head is None:
        return
    if c_list.head.next is None:
        c_list.head = None
        return
    temp = c_list.head
    temp.data = temp.next.data
    temp.next = temp.next.next


def delete_k_node(c_list, k):
    if c_list.head is None:
        return
    temp = c_list.head
    i = 1
    if i == k:
        delete_head(c_list)
        return
    while i < k and temp != c_list.head:
        if i+1 == k:
            temp.next = temp.next.next
        temp = temp.next
        i += 1


def main():
    c_list = CircularLinkedList()
    c_list.head = Node(10)
    second = Node(20)
    third = Node(30)

    c_list.head.next = second
    second.next = third
    third.next = c_list.head
    c_list.print_list()

    insert_begin(c_list, Node(78))
    c_list.print_list()

    insert_end(c_list, Node(97))
    c_list.print_list()

    delete_head(c_list)
    c_list.print_list()

    delete_k_node(c_list, 1)
    c_list.print_list()


if __name__ == "__main__":
    main()
