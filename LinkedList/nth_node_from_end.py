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


def nth_node_end(l_list, n):
    if l_list.head is None:
        return
    temp = l_list.head
    count_n = 0
    while temp:
        count_n += 1
        temp = temp.next
    if count_n < n:
        return
    j = 1
    node_loc = count_n - n + 1
    n_temp = l_list.head
    while j <= node_loc and n_temp:
        if j == node_loc:
            print(n, "Node from end is: ", n_temp.data)
            return
        n_temp = n_temp.next
        j += 1


""" Efficient Solution using two pointers and giving one pointer lead by n """


def nth_node_eff(l_list, n):
    if l_list.head is None:
        return
    temp = l_list.head
    i = 1
    while i < n:
        if temp is None:
            return
        temp = temp.next
        i += 1
    n_temp = l_list.head
    while temp:
        if temp.next is None:
            print(n, "Node from the end is: ", n_temp.data)
        n_temp = n_temp.next
        temp = temp.next


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
    nth_node_end(l_list, 3)
    nth_node_eff(l_list, 3)


if __name__ == '__main__':
    # Start with the empty list
    main()
