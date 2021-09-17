""" Next Greater Element: """


def easy_next_greater(arr_in):
    res = [-1] * len(arr_in)
    for i in range(len(arr_in)-1):
        for j in range(i+1, len(arr_in)):
            if arr_in[j] > arr_in[i]:
                res[i] = arr_in[j]
                break
    return res


def next_greater_e(arr_in):
    span_arr = [-1] * len(arr_in)
    stack = [arr_in[len(arr_in)-1]]
    for i in range(len(arr_in)-2, -1, -1):
        if arr_in[i] < stack[len(stack)-1]:
            span_arr[i] = stack[len(stack)-1]
            stack.append(arr_in[i])
        else:
            while len(stack) > 0 and arr_in[i] > stack[len(stack)-1]:
                stack.pop()
            span_arr[i] = -1 if len(stack) == 0 else stack[len(stack)-1]
            stack.append(arr_in[i])
    return span_arr


def main():
    price_input = [5, 15, 10, 8, 6, 12, 9, 18]
    print(next_greater_e(price_input))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
