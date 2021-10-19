""" Self Balancing trees: Find the ceiling of the element in the left side of the array """
from sortedcontainers import SortedSet


def ceil_left(arr_in):
    n_arr = [-1] * len(arr_in)
    nums = SortedSet()
    for i in range(len(arr_in)):
        if arr_in[i] in nums:
            n_arr[i] = arr_in[i]
        else:
            if nums.bisect_left(arr_in[i]) < len(nums):
                n_arr[i] = nums[nums.bisect_left(arr_in[i])]
            nums.add(arr_in[i])
    return n_arr


def main():
    arr = [6, 18, 4, 5]
    print(ceil_left(arr))


if __name__ == "__main__":
    main()
