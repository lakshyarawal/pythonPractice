""" Count Set Bits: Find number of bits set as 1 in the binary representation of given decimal number """

"""Solution: Count the last bit and increment by setting MSB as 0"""


def count_set_bits(a) -> int:
    count_bits = 0
    while a > 0:
        if a & 1 != 0:
            count_bits += 1
            # This if condition could be replaced by count_bits = count_bits + ( a & 1)
        a = a >> 1
    return count_bits


"""Brian Kerningam's Algo: When you subtract 1 from a number all numbers before the first set bit become 1 and last set bit is 0 
   and when you AND it with the original number the last bit gets turned off"""


def bk_algo(a) -> int:
    count_bk_bits = 0
    while a > 0:
        count_bk_bits += 1
        a = a & (a-1)
    return count_bk_bits


"""Lookup Table Method: In preprocessing divide 32 bit number into 8 bit chunks. 8 bits have max value 2^7 -1.
   So you need lookup table for numbers up to 255. You do this process 4 times and keep adding the result"""


def look_up_table(a) -> int:
    table = [0] * 256
    table[0] = 0
    for i in range(1, len(table)):
        table[i] = (i & 1) + table[i//2]
    count_bk_bits = table[a & 0xff]
    a = a >> 8
    count_bk_bits = count_bk_bits + table[a & 0xff]
    a = a >> 8
    count_bk_bits = count_bk_bits + table[a & 0xff]
    a = a >> 8
    count_bk_bits = count_bk_bits + table[a & 0xff]
    return count_bk_bits


def main():
    val1 = int(input("Enter your value: "))
    ans = count_set_bits(val1)
    ans_bk = bk_algo(val1)
    ans_lt = look_up_table(val1)
    print(ans)
    print(ans_bk)
    print(ans_lt)


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
