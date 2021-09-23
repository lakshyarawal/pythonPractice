""" Deleting a Node without a head pointer """


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


def delete_middle(middle_node):
    middle_node.data = middle_node.next.data
    middle_node.next = middle_node.next.next


def main():
    l_list = LinkedList()

    l_list.head = Node(10)
    second = Node(20)
    third = Node(30)
    fourth = Node(40)

    l_list.head.next = second
    second.next = third  # Link second node with the third node
    third.next = fourth
    delete_middle(third)
    l_list.print_list()


if __name__ == '__main__':
    # Start with the empty list
    main()
