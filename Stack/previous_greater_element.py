""" Previous Greater Element: """


def easy_greater(arr_in):
    res = [-1] * len(arr_in)
    for i in range(1, len(arr_in)):
        for j in range(i-1, -1, -1):
            if arr_in[j] > arr_in[i]:
                res[i] = arr_in[j]
                break
    return res


def previous_greater_e(arr_in):
    span_arr = [-1] * len(arr_in)
    stack = [arr_in[0]]
    for i in range(1, len(arr_in)):
        if arr_in[i] < stack[len(stack)-1]:
            span_arr[i] = stack[len(stack) - 1]
            stack.append(arr_in[i])
        else:
            while len(stack) > 0 and arr_in[i] > stack[len(stack)-1]:
                stack.pop()
            span_arr[i] = -1 if len(stack) == 0 else stack[len(stack)-1]
            stack.append(arr_in[i])
    return span_arr


def main():
    price_input = [15, 10, 18, 12, 4, 6, 2, 8]
    print(previous_greater_e(price_input))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
