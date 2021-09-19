""" Converting an postfix expression into output value"""


def check_precedence(op):
    operators = ['(', ')', '^', '*', '/', '+', '-']
    has_op = {'(': 0, ')': 0, '^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    for i in range(len(operators)):
        if op == operators[i]:
            return has_op[operators[i]]
    return -1


def operation(op1, op2, op_tn):
    res = 0
    a = int(op1)
    b = int(op2)
    if op_tn == '+':
        res = a+b
    elif op_tn == '-':
        res = a-b
    elif op_tn == '*':
        res = a*b
    elif op_tn == '/':
        res = a/b
    elif op_tn == '^':
        res = pow(a, b)
    return res


def find_post_val(str_input):
    operators = ['(', ')', '^', '*', '/', '+', '-']
    op_stack = []
    curr_in = ""
    # Iterate through the string from right to left, if you find an operator push it into the stack
    for i in range(len(str_input)):
        if str_input[i] == " ":
            if curr_in in operators:
                op_2 = op_stack.pop()
                op_1 = op_stack.pop()
                post_res = operation(op_1, op_2, curr_in)
                op_stack.append(post_res)
            else:
                op_stack.append(curr_in)
            curr_in = ""
        else:
            curr_in += str_input[i]
    return op_stack.pop()


def main():
    str_input = "10 2 * 3 5 * + 9 - "
    print(find_post_val(str_input))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
