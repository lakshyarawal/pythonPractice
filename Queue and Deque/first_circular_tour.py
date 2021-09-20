""" Finding the First Circular tour """
from collections import deque


def first_circular_t(p_a, d_a):
    d_q = deque(d_a)
    p_q = deque(p_a)
    curr_count = 0
    i = 1
    carry = 0
    if sum(p_a) < sum(d_a):
        return -1
    while curr_count < len(p_a):
        p_1 = p_q.popleft()
        d_1 = d_q.popleft()
        if p_1 + carry >= d_1:
            curr_count += 1
            carry += p_1 - d_1
            p_q.append(p_1)
            d_q.append(d_1)
            print(p_q, curr_count, carry)
        else:
            carry = 0
            p_q.append(p_1)
            d_q.append(d_1)
            curr_count = 0
            i += 1
    return i


""" We can do the same using pointers too """


def first_circular_t_eff(p_a, d_a):
    start = 0
    curr_pet = 0
    prev_pet = 0
    i = 0
    while i < len(p_a):
        curr_pet += p_a[i] - d_a[i]
        if curr_pet < 0:
            start = i + 1
            prev_pet += curr_pet
            curr_pet = 0
        i += 1
    return start + 1 if curr_pet + prev_pet >= 0 else -1


def main():
    petrol = [4, 9, 40]
    dist = [5, 10, 12]
    print(first_circular_t_eff(petrol, dist))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
