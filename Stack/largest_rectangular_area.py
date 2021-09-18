""" Finding the Largest Rectangular Area in a histogram:  """


def easy_area(arr_in):
    res = arr_in[0]
    for i in range(len(arr_in)):
        res = max(res, arr_in[i])
        min_el = arr_in[i]
        for j in range(i+1, len(arr_in)):
            min_el = min(min_el, arr_in[i], arr_in[j])
            res = max(res, min_el*(j-i+1))
    return res


""" Efficient approach based on previous smaller and next smaller elements"""


def rec_area(arr_in):
    res = 0
    stack = []
    for i in range(len(arr_in)):
        while len(stack) > 0 and arr_in[stack[len(stack)-1]] >= arr_in[i]:
            tp = stack.pop()
            curr = arr_in[tp]*i if len(stack) == 0 else arr_in[tp]*(i-stack[len(stack)-1]-1)
            res = max(res, curr)
        stack.append(i)
    print(stack)
    while len(stack) > 0:
        tp = stack.pop()
        curr = arr_in[tp]*len(arr_in) if len(stack) == 0 else arr_in[tp]*(len(arr_in)-stack[len(stack)-1]-1)
        res = max(res, curr)
    return res


def main():
    arr_input = [6, 2, 5, 4, 1, 5, 6]
    print(rec_area(arr_input))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
