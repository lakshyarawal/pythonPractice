""" Finding the Intersection of two linked list:  """


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
        print(" ")


def find_intersection(l_list1, l_list2):
    l_list1.print_list()
    l_list2.print_list()
    h_1 = l_list1.head
    h_2 = l_list2.head
    h_1_set = {h_1: 1}
    while h_1:
        h_1 = h_1.next
        h_1_set[h_1] = 1
    while h_2:
        if h_2 in h_1_set.keys():
            print(h_2.data)
            return
        h_2 = h_2.next


def find_intersection_eff(l_list1, l_list2):
    h_1 = l_list1.head
    h_2 = l_list2.head
    count_1, count_2 = 0, 0
    while h_1:
        count_1 += 1
        h_1 = h_1.next

    while h_2:
        count_2 += 1
        h_2 = h_2.next

    step = abs(count_2-count_1)
    count_1_head = l_list1.head
    count_2_head = l_list2.head
    if count_1 > count_2:
        while step:
            count_1_head = count_1_head.next
            step -= 1
    else:
        while step:
            count_2_head = count_2_head.next
            step -= 1

    while count_1_head and count_2_head:
        if count_1_head == count_2_head:
            print(count_2_head.data)
            break
        count_1_head = count_1_head.next
        count_2_head = count_2_head.next


def main():
    l_list = LinkedList()
    n_list = LinkedList()
    n_list.head = Node(44)
    l_list.head = Node(10)
    second = Node(20)
    third = Node(30)
    fourth = Node(40)

    l_list.head.next = second
    second.next = third  # Link second node with the third node
    third.next = fourth
    n_list.head.next = third
    find_intersection_eff(l_list, n_list)


if __name__ == '__main__':
    # Start with the empty list
    main()
