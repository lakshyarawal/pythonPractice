""" Josephus Problem: In a circle on N [0, 1, ... N-1 ] people we have to kill the Kth person and find the survivor """

"""Solution: """


def jp_problem(n, k) -> int:
    if n == 1:
        return 0
    return (jp_problem(n - 1, k) + k) % n


def main():
    people = int(input("Enter number of people: "))
    kill_k = int(input("Enter which person to kill: "))
    print(jp_problem(people, kill_k))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
