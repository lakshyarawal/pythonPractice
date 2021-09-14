""" Detecting Loop in a given linked list """


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


def detect_loop(l_list):
    if l_list.head is None:
        print("Null List")
        return
    if l_list.head.next is None:
        if l_list.head.next == l_list.head:
            print("Loop Present")
        return
    temp = l_list.head.next
    while temp:
        curr_head = l_list.head
        while curr_head:
            if curr_head == temp.next:
                print(curr_head.data, temp.data)
                print("Loop Present")
                return
            if curr_head == temp:
                break
            curr_head = curr_head.next
        temp = temp.next


""" Another approach would be to add a boolean visited in the Node class and mark it True. If we see any visited we 
    print that the loop is present as we already seen this element before"""

""" Another approach would be to create a dummy node and once you visit a node you change it's next to this dummy node
    If you visit this node again due to loop you would find the next as this dummy node. """

""" To do this without modifying the linked list we can use a hash set """


def detect_loop_hash(l_list):
    if l_list.head is None:
        return
    temp = l_list.head
    hash_set = {temp: 1}
    while temp:
        temp = temp.next
        if temp in hash_set.keys():
            print(temp.data)
            print("Loop Detected")
            return
        else:
            hash_set[temp] = 1


""" To do this with O(1) aux space we can use the floyd cycle detection algorithm. Also to remove the loop we can use 
    the fact that when these two pointers meet if we reset slow to head and move them again at the same speed they
    will meet at the beginning of the loop"""


def detect_loop_floyd(l_list):
    if l_list.head is None:
        return
    s_head = l_list.head
    f_head = l_list.head
    while f_head and f_head.next:
        s_head = s_head.next
        f_head = f_head.next.next
        if s_head == f_head:
            break
    if s_head != f_head:
        return
    s_head = l_list.head
    while f_head.next != s_head.next:
        f_head = f_head.next
        s_head = s_head.next
    f_head.next = None


def main():
    l_list = LinkedList()

    l_list.head = Node(10)
    second = Node(20)
    third = Node(30)
    fourth = Node(40)

    l_list.head.next = second
    second.next = third  # Link second node with the third node
    third.next = fourth
    fourth.next = second
    detect_loop_floyd(l_list)
    l_list.print_list()


if __name__ == '__main__':
    # Start with the empty list
    main()
