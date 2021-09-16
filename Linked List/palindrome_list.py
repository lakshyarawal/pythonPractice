""" Palindrome List  """
from reverse_list import LinkedList, Node


def is_palindrome(l_list):
    if l_list.head is None or l_list.head.next is None:
        return
    slow_node = l_list.head
    fast_node = l_list.head
    # Find Length of List
    while fast_node.next and fast_node.next.next:
        slow_node = slow_node.next
        fast_node = fast_node.next.next
    rev = l_list.reverse(slow_node.next)
    curr_node = l_list.head
    while rev:
        if rev.data != curr_node.data:
            print("Not a palindrome")
            return
        rev = rev.next
        curr_node = curr_node.next
    print("Looks like a palindrome")
    return


def main():
    l_list = LinkedList()

    l_list.head = Node('R')
    second = Node('A')
    third = Node('D')
    fourth = Node('A')
    fifth = Node('R')

    l_list.head.next = second
    second.next = third  # Link second node with the third node
    third.next = fourth
    fourth.next = fifth

    l_list.print_list()
    is_palindrome(l_list)


if __name__ == '__main__':
    # Start with the empty list
    main()
