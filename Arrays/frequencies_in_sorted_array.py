""" Frequencies in a Sorted Array:  print the frequency of each number in the sorted array
    Eg: I/P: [ 10, 10, 10, 25, 30, 30 ]  O/P: 10 3, 25 1, 30, 2"""

"""Solution:  """


def frequencies(a) -> list:
    n = len(a)
    freq_arr = []
    if n == 1:
        return [[a[0], 1]]
    curr_freq = 1
    for i in range(1, n):
        if a[i] == a[i-1]:
            curr_freq += 1
        else:
            freq_arr.append([a[i-1], curr_freq])
            curr_freq = 1
    freq_arr.append([a[n - 1], curr_freq])
    return freq_arr


def main():
    arr_input = [10, 20, 30, 30, 30]
    a = frequencies(arr_input)
    print(a)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
