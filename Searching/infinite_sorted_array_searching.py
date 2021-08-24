""" We are given an array on infinite size and we know that it is sorted. Return index of element if present"""
from binary_search import binary_search_iterative
""" Solution: """


def infinite_search(a, num) -> int:
    low = 0
    i = 1
    if a[low] == num:
        return low
    while True:
        if i > len(a)-1:
            i = len(a) - 1
        if a[i] == num:
            return i
        if a[i] > num:
            # Some low condition
            j = low + 1
            return j + binary_search_iterative(arr=a[j: i], num=num)
        if a[i] < num:
            low = i
            i = i * 2


def main():
    num_input = int(input("Enter a number here: "))
    arr = [10, 20, 40, 100, 200, 500, 600, 720, 800, 900, 1000, 1200, 12000, 13000]
    a2 = infinite_search(arr, num_input)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
