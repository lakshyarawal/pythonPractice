""" Given an integer find the square root of the number """

""" Solution: """


def square_root(num) -> int:
    high = num
    low = 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if mid * mid == num:
            return mid
        if mid * mid > num:
            high = mid - 1
        if mid * mid < num:
            low = mid + 1
            ans = mid
    return ans


def main():
    num_input = int(input("Enter a number here: "))
    a2 = square_root(num_input)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
