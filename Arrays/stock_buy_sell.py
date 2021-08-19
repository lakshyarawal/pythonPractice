""" """

"""Solution:  """


def stock_buy(a) -> int:
    n = len(a)
    if n == 1:
        return 0
    profit = 0
    current_min = a[0]
    current_max = a[1]
    for i in range(1, n):
        if a[i] > a[i-1]:
            current_max = a[i]
            continue
        else:
            profit = profit + current_max - current_min
            current_min = a[i]
        profit = profit - current_min
    profit = profit + current_max - current_min
    return profit


def main():
    arr_input = [1, 5, 3, 1, 2, 8]
    a = stock_buy(arr_input)
    print(a)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
