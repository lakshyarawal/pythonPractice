"""Repeating elements: All elements appear exactly once except one element, we have to find that element.
   Also all elements from 0 to max of the array are present at least once in the array. Eg: [0, 2, 1, 3, 2, 2] O/P: 2"""

""" Solution: """


def repeating_element(a) -> int:
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            if a[i] == a[j]:
                return a[i]


def repeating_element_2(a) -> int:
    n = len(a)
    temp_arr = [0]*n
    for i in range(n):
        temp_arr[a[i]] += 1
    for i in range(n):
        if temp_arr[i] > 1:
            return i
    return -1


""" More Efficient idea is to use a approach where we find cycles/loop in the array and we know that the repeating
    element would be the first node in this array"""


def repeating_element_eff(a) -> int:
    n = len(a)
    slow = a[0] + 1
    fast = a[0] + 1
    slow = a[slow] + 1
    fast = a[a[fast] + 1] + 1
    while slow != fast:
        slow = a[slow] + 1
        fast = a[a[fast] + 1] + 1
    slow = a[0] + 1
    while slow != fast:
        slow = a[slow] + 1
        fast = a[fast] + 1
    return slow - 1


def main():
    arr = [1, 2, 3, 3, 0, 4, 5]
    a2 = repeating_element_eff(arr)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
