""" Subset Sum: Given an array/set of integers and a sum value, count the number of subsets which add up to the sum
    Eg: { 10, 5, 2, 3, 6 } , Sum = 8 then the output will be: 2 for { 5, 3 } and { 2, 6 } """

"""Solution: Create a tree of options including and excluding the element and return 1 if subset sum is same"""


def subset_sum(n, s) -> int:
    if s == 0:
        return 1
    subset_count = 0
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            if n[i] + n[j] == s:
                subset_count += 1
    return subset_count


def subset_sum_eff(arr, n, s) -> int:
    if n == 0:
        return 1 if s == 0 else 0
    return subset_sum_eff(arr, n-1, s) + subset_sum_eff(arr, n-1, s - arr[n-1])


def main():
    parent_set = [10, 5, 2, 3, 6]
    sum_total = int(input("Enter total sum required: "))
    print(subset_sum(parent_set, sum_total))
    print(subset_sum_eff(parent_set, len(parent_set), sum_total))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
