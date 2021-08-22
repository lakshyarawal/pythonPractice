""" Maximum Consecutive Flips: In a binary array """

"""Solution:  """


def max_flips_eff(a):
    n = len(a)
    first_group = a[0]
    curr_flipping = False
    for i in range(1, n):
        if a[i] == first_group:
            if curr_flipping:
                print("to ", i-1)
                curr_flipping = False
            continue
        else:
            if curr_flipping:
                print("to ", i)
                curr_flipping = False
            else:
                print("flipping from", i, end = " ")
                curr_flipping = True
        if curr_flipping and i == n-1:
            print("to ", i)


def main():
    arr_input = [1, 1, 0, 0, 1, 1, 0, 0]
    max_flips_eff(arr_input)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
