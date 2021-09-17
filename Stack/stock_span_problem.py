""" Stock Span Problem: """


def easy_span(pr_in):
    sp_arr = [1] * len(pr_in)
    for i in range(1, len(pr_in)):
        curr_count = 1
        for j in range(i-1, -1, -1):
            if pr_in[j] < pr_in[i]:
                curr_count += 1
            else:
                break
        sp_arr[i] = curr_count
    return sp_arr


def stock_span(pr_in):
    span_arr = [1] * len(pr_in)
    stack = [0]
    for i in range(1, len(pr_in)):
        if pr_in[i] < stack[len(stack) - 1]:
            span_arr[i] = 1
            stack.append(i)
        else:
            while len(stack) > 0 and pr_in[stack[len(stack)-1]] <= pr_in[i]:
                stack.pop()
            span_arr[i] = i + 1 if len(stack) == 0 else i - stack[len(stack)-1]
            stack.append(i)
    return span_arr


def main():
    price_input = [13, 15, 12, 14, 16, 8, 6, 4, 10, 30]
    print(stock_span(price_input))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
