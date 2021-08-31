""" Meet Maximum guests at a party: You are given two arrays that denote the arrival and departure time of the
    guest and you have to print the mx guest you can meet. Time for party is 0 < t < 2359.
    Eg: arrival = [800, 700, 600, 500], departure = [840, 820, 830, 530] O/P: 3 (800 to 820)"""

"""Solution"""


def meet_guests(arrival, departure) -> int:
    arrival = sorted(arrival)
    departure = sorted(departure)
    arr_index = 1
    depart_index = 0
    total_guests = 1
    curr_guests = 1
    while arr_index < len(arrival) and depart_index < len(departure):
        if arrival[arr_index] <= departure[depart_index]:
            curr_guests += 1
            arr_index += 1
        else:
            curr_guests -= 1
            depart_index += 1
        total_guests = max(total_guests, curr_guests)
    return total_guests


def main():
    arrival = [800, 700, 600, 500]
    departure = [840, 820, 830, 530]
    a2 = meet_guests(arrival, departure)
    print(a2)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
