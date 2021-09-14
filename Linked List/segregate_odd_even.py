""" Segregate Odd and Even Values in Linked List such that all even values appear first, maintaining original order """


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


def seg_odd_even(l_list):
    if l_list.head is None or l_list.head.next is None:
        return
    cur_node = l_list.head
    odd_list = LinkedList()
    if cur_node.data % 2 != 0:
        n_node = Node(cur_node.data)
        last_odd_node = n_node
        odd_list.head = n_node
        l_list.head = l_list.head.next
    else:
        last_odd_node = None
    while cur_node.next is not None:
        if cur_node.next.data % 2 != 0:
            n_node = Node(cur_node.next.data)
            if odd_list.head is None:
                odd_list.head = n_node
                last_odd_node = odd_list.head
            else:
                last_odd_node.next = n_node
                last_odd_node = n_node
            cur_node.next = cur_node.next.next
        else:
            cur_node = cur_node.next
    temp = l_list.head
    while temp:
        if temp.next is None:
            temp.next = odd_list.head
            return
        temp = temp.next
    print("Odd List: ", end=" ")
    odd_list.print_list()


def seg_odd_even_eff(l_list):
    if l_list.head is None or l_list.head.next is None:
        return
    e_s, e_e = None, None
    o_s, o_e = None, None
    cur_node = l_list.head
    while cur_node is not None:
        if cur_node.data % 2 == 0:
            if e_s is None:
                e_s = cur_node
                e_e = e_s
            else:
                e_e.next = cur_node
                e_e = e_e.next
        else:
            if o_s is None:
                o_s = cur_node
                o_e = o_s
            else:
                o_e.next = cur_node
                o_e = o_e.next
        cur_node = cur_node.next
    if o_s is None or e_s is None:
        return
    e_e.next = o_s
    o_e.next = None
    new_list = LinkedList()
    new_list.head = e_s
    new_list.print_list()


def main():
    l_list = LinkedList()

    l_list.head = Node(11)
    second = Node(20)
    third = Node(31)
    fourth = Node(40)

    l_list.head.next = second
    second.next = third  # Link second node with the third node
    third.next = fourth
    seg_odd_even_eff(l_list)


if __name__ == '__main__':
    # Start with the empty list
    main()
