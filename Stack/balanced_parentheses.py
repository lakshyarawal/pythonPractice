""" Balanced Parentheses using Stack Data Structure """
from collections import deque


def is_balanced(str_input):
    stack = deque()
    open_br = ['(', '[', '{']
    close_br = [')', ']', '}']
    for i in range(len(str_input)):
        print(str_input[i], stack)
        if any(item == str_input[i] for item in open_br):
            stack.append(str_input[i])
        else:
            if len(stack) == 0:
                print("Parentheses are not balanced")
                return
            for j in range(len(close_br)):
                if str_input[i] == close_br[j]:
                    remove = stack.pop()
                    if remove != open_br[j]:
                        print("Parentheses are not balanced")
                        return
    if len(stack) > 0:
        print("Parentheses are not balanced")
        return
    print("Parentheses are balanced")


def main():
    str_input = "((())"
    is_balanced(str_input)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
