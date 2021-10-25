""" Purchasing maximum items using the given sum and prices """
import heapq


def max_items(arr_in, k):
    o_arr = []
    for i in range(len(arr_in)):
        heapq.heappush(o_arr, arr_in[i])
    curr_sum = 0
    items = 0
    while curr_sum <= k:
        curr_sum += heapq.heappop(o_arr)
        if curr_sum > k:
            break
        items += 1
    print(items)


def main():
    n_arr = [1, 12, 5, 111, 200]
    max_items(n_arr, 10)


if __name__ == "__main__":
    main()
