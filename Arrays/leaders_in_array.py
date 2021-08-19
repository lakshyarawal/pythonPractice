""" Leaders in Array: Given an array find Leaders (Element on the right are smaller than the num)  """

"""Solution:  """


def leaders(a) -> list:
    n = len(a)
    leader_list = []
    for i in range(n):
        bool_leader = True
        for j in range(i+1, n):
            if a[j] >= a[i]:
                bool_leader = False
        if bool_leader:
            leader_list.append(a[i])
    return leader_list


def leaders_eff(a) -> list:
    n = len(a)
    leader_list = [a[n - 1]]
    curr_leader = a[n-1]
    for i in range(n-2, 0, -1):
        if a[i] > curr_leader:
            leader_list.append(a[i])
            curr_leader = a[i]
    return leader_list


def main():
    arr_input = [7, 10, 4, 3, 6, 5, 2]
    a = leaders_eff(arr_input)
    print(a)
    a = leaders(arr_input)
    print(a)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
