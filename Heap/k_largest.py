"""Printing K largest elements in an array"""
import heapq


def k_largest(arr_in, k):
    o_arr = []
    for i in range(k):
        heapq.heappush(o_arr, arr_in[i])
    for i in range(k, len(arr_in)):
        if arr_in[i] > heapq.nsmallest(1, o_arr)[0]:
            heapq.heappop(o_arr)
            heapq.heappush(o_arr, arr_in[i])
    while len(o_arr) > 0:
        print(heapq.heappop(o_arr), end=" ")


def main():
    n_arr = [8, 6, 4, 10, 9]
    k_largest(n_arr, 3)


if __name__ == "__main__":
    main()
