""" Stock Buy and Sell: Given an array of prices find maximum profit using buy and sell variations """

"""Solution:  """


def stock_buy_rec(a, s, e) -> int:
    if e < s:
        return 0
    profit = 0
    for i in range(s, e):
        for j in range(i+1, e+1):
            if a[j] > a[i]:
                cur_profit = a[j] - a[i] + stock_buy_rec(a, s, i-1) + stock_buy_rec(a, j+1, e)
                profit = max(cur_profit, profit)
    return profit


def stock_buy_eff(a) -> int:
    profit = 0
    n = len(a)
    if n == 1:
        return 0
    for i in range(1, n):
        if a[i] > a[i-1]:
            profit += a[i] - a[i-1]
    return profit


def main():
    arr_input = [1, 5, 3, 8, 12]
    start = 0
    end = len(arr_input) - 1
    a2 = stock_buy_eff(arr_input)
    print(a2)
    a = stock_buy_rec(arr_input, start, end)
    print(a)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
