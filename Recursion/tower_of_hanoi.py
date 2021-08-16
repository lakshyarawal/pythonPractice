""" Tower of Hanoi: We have three towers, A, B and C. There are discs placed in tower A. Target is to move these discs
    from tower A to C, using tower B. The order should remain same, with largest on the bottom and smallest on top
    Rules: Only one disc can move at a time, Largest has to be at bottom in between steps also,Only move the top disc"""

"""Solution: We break down the problem for N - 1 and then move disc from A to C"""


def tower_of_hanoi(n, a, b, c):
    if n == 1:
        print("Move 1 from " + a + " to " + c)
        return
    tower_of_hanoi(n - 1, a, c, b)
    print("Move " + str(n) + " from " + a + " to " + c)
    tower_of_hanoi(n - 1, b, a, c)


def main():
    discs = int(input("Enter no. of discs: "))
    tower_of_hanoi(discs, "A", "B", "C")


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
