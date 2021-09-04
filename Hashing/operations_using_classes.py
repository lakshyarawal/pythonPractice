""" Basic Operations using Linked List and Node Classes """


class Node:
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


class LinkedList:

    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def searching_element(self, val) -> bool:
        temp = self.head
        while temp:
            if temp.data == val:
                return True
            temp = temp.next
        return False

    def inserting_element(self, val):
        temp = self.head
        new_node = Node(val)
        while temp:
            if temp.next:
                temp = temp.next
            else:
                temp.next = new_node
                return

    def deleting_element(self, val):
        temp = self.head
        if temp.data == val:
            self.head = temp.next
            return
        while temp.next:
            if temp.next.data == val:
                temp.next = temp.next.next
                return
            temp = temp.next
        return


def main():
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third
    llist.print_list()
    print(llist.searching_element(1))
    llist.inserting_element(5)
    llist.print_list()
    print("Deleting element: ")
    llist.deleting_element(5)
    llist.print_list()


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
