""" Implementation of LinkedList"""


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


def print_list_rec(node_input):
    if node_input is None:
        return
    print(node_input.data)
    print_list_rec(node_input.next)


def insert_at_begin(l_list, new_head):
    if l_list.head is None:
        l_list.head = new_head
        return
    temp = Node(l_list.head.data)
    temp.next = l_list.head.next
    l_list.head = new_head
    new_head.next = temp


def insert_at_end(l_list, new_node):
    if l_list.head is None:
        l_list.head = new_node
    temp = l_list.head
    while temp:
        if temp.next is None:
            temp.next = new_node
            return
        temp = temp.next


def delete_head(l_list):
    if l_list.head is None:
        return
    if l_list.head.next is None:
        l_list.head = None
        return
    l_list.head = l_list.head.next


def delete_at_end(l_list):
    if l_list.head is None:
        return
    if l_list.head.next is None:
        l_list.head = None
        return
    temp = l_list.head
    while temp.next:
        if temp.next.next is None:
            temp.next = None
            return
        temp = temp.next


def insert_at_pos(l_list, pos, data):
    temp = Node(data)
    if pos == 1:
        insert_at_begin(l_list, temp)
    if l_list.head is None:
        return
    cur_node = l_list.head
    i = 1
    while i < pos:
        if i+1 == pos:
            temp.next = cur_node.next
            cur_node.next = temp
        i += 1
        if cur_node.next is None:
            break
        cur_node = cur_node.next


def search_elem(l_list, e_data):
    temp = l_list.head
    i = 1
    while temp:
        if temp.data == e_data:
            return i
        temp = temp.next
        i += 1
    return -1


def main():
    llist = LinkedList()

    llist.head = Node(10)
    second = Node(20)
    third = Node(30)

    llist.head.next = second  # Link first node with second
    second.next = third  # Link second node with the third node
    print_list_rec(llist.head)
    insert_at_begin(llist, Node(5))
    insert_at_end(llist, Node(55))
    delete_head(llist)
    delete_at_end(llist)
    insert_at_pos(llist, 3, 99)
    print(search_elem(llist, 100))
    llist.print_list()


if __name__ == '__main__':
    # Start with the empty list
    main()
