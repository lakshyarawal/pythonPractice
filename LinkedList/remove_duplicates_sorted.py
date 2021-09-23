""" Removing duplicates from a sorted linked list:  """


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


def remove_duplicates(l_list):
    if l_list.head is None or l_list.head.next is None:
        return
    temp = l_list.head
    while temp and temp.next:
        if temp.data == temp.next.data:
            temp.next = temp.next.next
        else:
            temp = temp.next


def main():
    l_list = LinkedList()

    l_list.head = Node(10)
    second = Node(20)
    third = Node(30)
    fourth = Node(30)
    fifth = Node(40)
    sixth = Node(40)
    seventh = Node(40)

    l_list.head.next = second
    second.next = third  # Link second node with the third node
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = seventh

    l_list.print_list()
    remove_duplicates(l_list)
    l_list.print_list()


if __name__ == '__main__':
    # Start with the empty list
    main()
