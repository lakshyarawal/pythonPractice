"""LRU Cache Design using Linked List: """


class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
        self.prev = None


class DoubleLinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("")


def lru_cache(c, r_s):
    n_list = DoubleLinkedList()
    dict_cache = {}
    curr_cap = 1
    n_list.head = Node(r_s[0])
    dict_cache[n_list.head.data] = n_list.head
    # Iterate through the inputs from 1 and then check
    # 1. if curr cap is full
    # 2. If the element is present in dictionary
    # If cap is full and element is present in dictionary then move it to the head
    # If cap is not full increment the count create a new node and make it the head
    for i in range(1, len(r_s)):
        if r_s[i] in dict_cache.keys():
            cur_node = n_list.head
            while cur_node.data != r_s[i]:
                cur_node = cur_node.next
            t = Node(cur_node.data)
            if cur_node.next is None:
                cur_node.prev.next = None
            else:
                cur_node.prev.next = cur_node.next
            t.next = n_list.head
            n_list.head.prev = t
            n_list.head = t
        else:
            new_node = Node(r_s[i])
            new_node.next = n_list.head
            n_list.head.prev = new_node
            n_list.head = new_node
            dict_cache[n_list.head.data] = n_list.head
            if curr_cap >= c:
                cur_node = n_list.head
                while cur_node:
                    if cur_node.next is None:
                        cur_node.prev.next = None
                        dict_cache.pop(cur_node.data)
                        break
                    cur_node = cur_node.next
            else:
                curr_cap += 1
        print("Curr Input: ", r_s[i], end=" Output: ")
        n_list.print_list()


def main():
    capacity = 4
    ref_seq = [10, 20, 10, 30, 40, 50, 30, 40, 60, 30]
    lru_cache(capacity, ref_seq)


if __name__ == '__main__':
    # Start with the empty list
    main()
