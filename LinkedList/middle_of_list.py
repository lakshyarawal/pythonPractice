""" Finding the Middle of the LinkedList. If two middle are present return the second one """


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


"""Naive approach using 2 traversals"""


def find_middle(l_list):
    if l_list.head is None:
        return
    if l_list.head.next is None:
        print(l_list.head.data)
        return
    temp = l_list.head
    i = 0
    while temp:
        i += 1
        temp = temp.next
    mid = i//2 + 1
    n_temp = l_list.head
    j = 1
    while j <= mid and n_temp:
        if j == mid:
            print("Middle Node: ", n_temp.data)
            return
        j += 1
        n_temp = n_temp.next


""" Efficient Solution"""


def find_middle_eff(l_list):
    if l_list.head is None:
        return
    if l_list.head.next is None:
        print(l_list.head.data)
        return
    temp = l_list.head
    s_temp = l_list.head
    while s_temp:
        s_temp = s_temp.next
        temp = temp.next.next
        if temp is None or temp.next is None:
            print("Middle Node: ", s_temp.data)
            return


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
    find_middle_eff(l_list)


if __name__ == '__main__':
    # Start with the empty list
    main()
