""" Converting an infix expression into Postfix expression"""
from collections import deque


def check_precedence(op):
    operators = ['(', ')', '^', '*', '/', '+', '-']
    has_op = {'(': 0, ')': 0, '^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    for i in range(len(operators)):
        if op == operators[i]:
            return has_op[operators[i]]
    return -1


def convert_post(str_input):
    post_res = ""
    operators = ['(', ')', '^', '*', '/', '+', '-']
    stack = []
    for i in range(len(str_input)):
        if str_input[i] not in operators:
            post_res += str_input[i]
        else:
            if len(stack) == 0:
                stack.append(str_input[i])
            else:
                pr = stack[len(stack) - 1]
                a = check_precedence(pr)
                b = check_precedence(str_input[i])
                if str_input[i] == ')' or a == b:
                    while len(stack) > 0:
                        m = stack.pop()
                        if m == '(':
                            continue
                        post_res += m
                    if str_input[i] != ')':
                        stack.append(str_input[i])
                    continue
                # Check precedence form stack top
                if b > a:
                    stack.append(str_input[i])
                else:
                    while len(stack) > 0:
                        m = stack.pop()
                        post_res += m
                    stack.append(str_input[i])
    while len(stack) > 0:
        m = stack.pop()
        post_res += m
    return post_res


def main():
    str_input = "a+b/c-d*e"
    print(convert_post(str_input))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
