""" Swapping Nodes pairwise: """


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


def pairwise_swap(l_list):
    if l_list.head is None or l_list.head.next is None:
        return
    curr_node = l_list.head.next.next
    prev = l_list.head
    l_list.head = l_list.head.next
    l_list.head.next = prev
    # A loop to iterate through elements swapping them and keeping track of next node
    while curr_node and curr_node.next:
        prev.next = curr_node.next
        prev = curr_node
        next_node = curr_node.next.next
        curr_node.next.next = curr_node
        curr_node = next_node
    prev.next = curr_node


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
    pairwise_swap(l_list)
    l_list.print_list()


if __name__ == '__main__':
    # Start with the empty list
    main()
