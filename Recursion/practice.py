""" """


""" Solution: """


def rec_list(a, lst) -> list:
    if a == 0:
        return []
    rec_list(a-1, lst)
    lst.append(a)
    return lst


def main():
    final_lst = []
    int_input = int(input("Enter a number : "))
    ans_eff = rec_list(int_input, final_lst)
    a = fib_rec(int_input)
    b = sum_natural(int_input)
    print(ans_eff)
    print(a)
    print(b)


def fact(n, fact_num):
    if n == 0 or n == 1:
        return 1
    fact_num = fact_num * n
    return fact(n-1, fact_num)


def fib_rec(a):
    if a == 0:
        return 0
    if a == 1:
        return 1
    return fib_rec(a-1) + fib_rec(a-2)


def sum_natural(a):
    if a == 0:
        return 0
    return a + sum_natural(a-1)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()