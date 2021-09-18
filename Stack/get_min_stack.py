""" Get Min using Stacks:  """

from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self):
        self.head = Node("head")
        self.size = 0
        self.min_stack1 = deque()
        self.min_el = 0

    # String representation of the stack
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]

        # Get the current size of the stack
    def get_size(self):
        return self.size

    # Check if the stack is empty
    def is_empty(self):
        return self.size == 0

    # Get the top item of the stack
    def peek(self):

        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.is_empty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value

    # Push a value into the stack.
    def push(self, value):
        if self.size == 0:
            self.min_el = value
        if value < self.min_el:
            self.min_stack1.append(value-self.min_el)
            self.min_el = value
        if len(self.min_stack1) == 0:
            self.min_stack1.append(value)
        if self.min_stack1[len(self.min_stack1)-1] >= value:
            self.min_stack1.append(value)
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def get_min(self):
        print(self.min_stack1[len(self.min_stack1)-1])

    # Remove a value from the stack and return.
    def pop(self):
        if self.is_empty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        if remove.value < 0:
            self.min_el = self.min_el - remove.value
            remove.value = remove.value + self.min_el
        if remove.value == self.min_stack1[len(self.min_stack1)-1]:
            self.min_stack1.pop()
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value


def main():
    s_i = Stack()
    s_i.push(20)
    s_i.push(10)
    s_i.get_min()
    s_i.push(5)
    s_i.get_min()
    s_i.pop()
    s_i.get_min()
    s_i.pop()
    s_i.get_min()


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
