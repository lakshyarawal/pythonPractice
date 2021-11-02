"""We are given k sorted arrays which we have to merge """
import heapq


def marge_k_arr(arr_in):
    o_arr = []
    fin_arr = []
    for k in range(len(arr_in)):
        heapq.heappush(o_arr, [arr_in[k][0], k, 0])
    while len(o_arr) > 0:
        curr_ele = heapq.heappop(o_arr)
        fin_arr.append(curr_ele[0])
        if curr_ele[2]+1 < len(arr_in[curr_ele[1]]):
            heapq.heappush(o_arr, [arr_in[curr_ele[1]][curr_ele[2]+1], curr_ele[1], curr_ele[2]+1])
    print(fin_arr)


def main():
    arr = [[10, 20, 30], [5, 15], [1, 9, 11, 18]]
    marge_k_arr(arr)


if __name__ == "__main__":
    main()
