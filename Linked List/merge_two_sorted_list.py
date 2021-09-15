""" Combine two sorted Linked List in place such that the result is also sorted """


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


def merge_list(l_list1, l_list2):
    l_list1.print_list()
    l_list2.print_list()
    h_1 = l_list1.head
    h_2 = l_list2.head
    # compare the data of two current nodes, if 1 > 2 then 2.next will be 1 and 2.next will be temp set as 1.next
    # Termination happens when you reach the end of smaller list
    if h_1.data > h_2.data:
        sm_h = l_list1.head
        la_h = l_list2.head
    else:
        la_h = l_list1.head
        sm_h = l_list2.head
    print(sm_h.data)
    while sm_h:
        while la_h.next and sm_h.data > la_h.next.data:
            la_h = la_h.next
            if la_h.next is None:
                la_h.next = sm_h
                return
        t = sm_h.next
        t2 = la_h.next
        la_h.next = sm_h
        sm_h.next = t2
        sm_h = t


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
    n_list = LinkedList()
    n_list.head = Node(2)
    new_node1 = Node(3)
    new_node2 = Node(4)
    n_list.head.next = new_node1
    new_node1.next = new_node2
    merge_list(l_list, n_list)
    l_list.print_list()
    n_list.print_list()


if __name__ == '__main__':
    # Start with the empty list
    main()
