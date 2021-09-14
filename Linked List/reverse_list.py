"""Reversing the elements of the given linked list """


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

    def reverse(self, head):

        # If head is empty or has reached the list end
        if head is None or head.next is None:
            return head

        # Reverse the rest list
        rest = self.reverse(head.next)

        # Put first element at the end
        head.next.next = head
        head.next = None

        # Fix the header pointer
        return rest


""" One approach would be to copy the elements into the array and then when you traverse the linked list again, you copy
    the element again in the nodes"""


def reverse_list(l_list):
    if l_list.head is None or l_list.head.next is None:
        return
    prev_node = None
    curr_node = l_list.head
    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    l_list.head = prev_node


def main():
    l_list = LinkedList()

    l_list.head = Node(10)
    second = Node(20)
    third = Node(30)
    fourth = Node(40)

    l_list.head.next = second
    second.next = third  # Link second node with the third node
    third.next = fourth

    l_list.print_list()
    reverse_list(l_list)
    l_list.print_list()
    l_list.head = l_list.reverse(l_list.head)
    l_list.print_list()


if __name__ == '__main__':
    # Start with the empty list
    main()
