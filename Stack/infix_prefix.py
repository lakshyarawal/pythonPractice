""" Converting an infix expression into Postfix expression"""


def check_precedence(op):
    operators = ['(', ')', '^', '*', '/', '+', '-']
    has_op = {'(': 0, ')': 0, '^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    for i in range(len(operators)):
        if op == operators[i]:
            return has_op[operators[i]]
    return -1


def convert_pre(str_input):
    pres_res = ""
    operators = ['(', ')', '^', '*', '/', '+', '-']
    stack = []
    for i in range(len(str_input)-1, -1, -1):
        if str_input[i] not in operators:
            pres_res += str_input[i]
        else:
            if len(stack) == 0:
                stack.append(str_input[i])
            else:
                pr = stack[len(stack) - 1]
                a = check_precedence(pr)
                b = check_precedence(str_input[i])
                if str_input[i] == '(' or a == b:
                    while len(stack) > 0:
                        m = stack.pop()
                        if m == ')':
                            continue
                        pres_res += m
                    if str_input[i] != '(':
                        stack.append(str_input[i])
                    continue
                # Check precedence form stack top
                elif b > a:
                    stack.append(str_input[i])
                else:
                    while len(stack) > 0:
                        if check_precedence(stack[len(stack)-1]) == b:
                            break
                        m = stack.pop()
                        pres_res += m
                    stack.append(str_input[i])
    while len(stack) > 0:
        m = stack.pop()
        pres_res += m
    return pres_res[::-1]


def main():
    str_input = "x+y/z-w*u"
    print(convert_pre(str_input))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
