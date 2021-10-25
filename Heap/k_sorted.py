"""Sort a k sorted array """
import heapq


def k_sorted(arr_in, k):
    o_arr = []
    for i in range(k+1):
        heapq.heappush(o_arr, arr_in[i])
    index = 0
    for i in range(k+1, len(arr_in)):
        arr_in[index] = heapq.heappop(o_arr)
        index += 1
        heapq.heappush(o_arr, arr_in[i])
    while len(o_arr) > 0:
        arr_in[index] = heapq.heappop(o_arr)
        index += 1
    print(arr_in)


def main():
    n_arr = [10, 9, 7, 8, 4, 70, 50, 60]
    k_sorted(n_arr, 4)


if __name__ == "__main__":
    main()
