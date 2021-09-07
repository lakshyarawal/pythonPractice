
""" Longest Consecutive Sub array: All numbers that come one after the other in a array """


def long_consecutive_sub(arr) -> int:
    result = 1
    set_ar = set(arr)
    for i in set_ar:
        if i - 1 not in set_ar:
            curr = 1
            while i + curr in set_ar:
                curr += 1
            result = max(result, curr)
    return result


def main():
    arr_input = [1, 20, 9, 3, 4, 2, 7]
    print(long_consecutive_sub(arr_input))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
