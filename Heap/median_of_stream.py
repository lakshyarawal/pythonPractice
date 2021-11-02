"""Median of a Stream: Given an array find the median at all points of the array """
import heapq


def median_arr(arr_in):
    o_arr = []
    x = 0
    while x < len(arr_in):
        heapq.heappush(o_arr, arr_in[x])
        curr_len = len(o_arr)
        if curr_len % 2 == 0:
            print((heapq.nsmallest(curr_len//2, o_arr)[curr_len//2-1]+heapq.nsmallest((curr_len//2)+1, o_arr)[curr_len//2])/2, end=" ")
        else:
            print(heapq.nsmallest((curr_len//2)+1, o_arr)[(curr_len//2)], end=" ")
        x += 1


def main():
    arr = [25, 7, 10, 15, 20]
    median_arr(arr)


if __name__ == "__main__":
    main()
