""" Trapping rain water: Given an array of non negative integers, they are height of bars.
    Find how much water can you collect between there bars """

"""Solution:  """


def rain_water(a) -> int:
    n = len(a)
    res = 0
    for i in range(1, n-1):
        lmax = a[i]
        for j in range(i):
            lmax = max(lmax, a[j])
        rmax = a[i]
        for j in range(i+1, n):
            rmax = max(rmax, a[j])
        res = res + (min(lmax, rmax) - a[i])
    return res


def rain_water_eff(a) -> int:
    n = len(a)
    res = 0
    lmax = [0]*n
    rmax = [0]*n
    lmax[0] = a[0]
    for i in range(1, n):
        lmax[i] = max(lmax[i-1], a[i])
    rmax[n-1] = a[n-1]
    for i in range(n-2, 0, -1):
        rmax[i] = max(rmax[i + 1], a[i])
    for i in range(1, n-1):
        res = res + min(lmax[i], rmax[i]) - a[i]
    return res


def main():
    arr_input = [5, 0, 6, 2, 3]
    a1 = rain_water_eff(arr_input)
    print(a1)
    a2 = rain_water(arr_input)
    #print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
