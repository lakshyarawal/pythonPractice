"""Two Pointer Approach: In an unsorted array we are given a number X, we have to find if there exists a pair
    such that the sum of pair is equal to X. Eg: [3, 5, 9, 2, 8, 10, 11] X = 17, O/P: Pair (9,8)
    Unsorted array can be solved using hashing, while sorted can be solved using two pointer approach
    Approach: move two pointers from left and right and then compare with sum and move again"""

""" Solution: """


def two_pointer(a, num) -> tuple:
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            if a[i] + a[j] == num:
                return a[i], a[j]
    return -1, -1


def two_pointer_eff(a, num) -> tuple:
    n = len(a)
    left = 0
    right = n-1
    while left < right:
        if a[left] + a[right] == num:
            return a[left], a[right]
        if a[left] + a[right] > num:
            right = right - 1
        else:
            left = left + 1
    return -1, -1


def two_pointer_triplet(a, num) -> tuple:
    left = 0
    right = 0
    n = len(a)
    i = 0
    while i < n:
        num = num - a[i]
        n = len(a[i:])
        left = 0
        right = n-1
        while left < right:
            if a[left] + a[right] == num:
                return a[left], a[right], a[i]
            if a[left] + a[right] > num:
                right = right - 1
            else:
                left = left + 1
        i = i + 1
    return a[left], a[right], a[i]


""" Alternative question: Find if there is a triplet that satisfies the pythagorean theorem : a^2 + b^2 = c^2"""


def main():
    num_input = 32
    arr = [2, 4, 8, 9, 10, 11, 12, 20, 30]
    a1, a2, a3 = two_pointer_triplet(arr, num_input)
    print(a1, a2, a3)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
