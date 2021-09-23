""" Inserting an Element in a sorted LinkedList so that the linked list remains sorted """


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


def insert_new(l_list, new_node):
    if l_list.head is None:
        l_list.head = new_node
        return
    temp = l_list.head
    if new_node.data < temp.data:
        new_node.next = temp
        l_list.head = new_node
    while new_node.data > temp.data:
        if temp.next is None:
            temp.next = new_node
            return
        if temp.next.data > new_node.data:
            new_node.next = temp.next
            temp.next = new_node
            return
        temp = temp.next


def main():
    l_list = LinkedList()

    l_list.head = Node(10)
    second = Node(20)
    third = Node(30)

    l_list.head.next = second
    second.next = third  # Link second node with the third node

    l_list.print_list()
    insert_new(l_list, Node(15))
    l_list.print_list()




if __name__ == '__main__':
    # Start with the empty list
    main()
