"""Printing K closest elements in an array"""
import heapq


def k_closest(arr_in, x, k):
    n_arr = arr_in.copy()
    for i in range(len(arr_in)):
        arr_in[i] = abs(arr_in[i]-x)
    o_arr = []
    for i in range(len(arr_in)):
        heapq.heappush(o_arr, [arr_in[i], i])
    for i in range(k):
        print(n_arr[heapq.heappop(o_arr)[1]], end=" ")


def main():
    n_arr = [10, 15, 7, 3, 4]
    k_closest(n_arr, 8, 2)


if __name__ == "__main__":
    main()
