""" Finding the Largest Rectangular Area in a histogram:  """


""" Naive Approach here is that you should find the area with every element as the smallest bar"""


def easy_area(arr_in):
    res = 0
    for i in range(len(arr_in)):
        area = arr_in[i]
        k = i - 1
        while k >= 0:
            if arr_in[k] >= arr_in[i]:
                area += arr_in[i]
            else:
                break
            k -= 1
        j = i+1
        while j < len(arr_in):
            if arr_in[j] >= arr_in[i]:
                area += arr_in[i]
            else:
                break
            j += 1
        print(arr_in[i], area)
        res = max(res, area)
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
