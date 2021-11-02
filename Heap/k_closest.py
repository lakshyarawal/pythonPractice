"""Printing K closest elements in an array"""
import heapq


def k_closest(arr_in, x, k):
    o_arr = []
    for i in range(len(arr_in)):
        heapq.heappush(o_arr, [abs(arr_in[i]-x), i])
    for i in range(k):
        print(arr_in[heapq.heappop(o_arr)[1]], end=" ")


def main():
    n_arr = [10, 15, 7, 3, 4]
    k_closest(n_arr, 8, 2)


if __name__ == "__main__":
    main()
