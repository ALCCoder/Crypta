"""

"""
import math


def get_bit_k_pos(number: int, k: int) -> int:
    #
    return number & (1 << (k - 1))


def change_bit_k_pos(number: int, k: int) -> int:
    #
    return number ^ (1 << (k - 1))


def swap_bits(number, ipos, jpos):
    #
    fbit = get_bit_k_pos(number, ipos)
    sbit = get_bit_k_pos(number, jpos)

    if fbit == sbit:
        return number

    return number ^ ((1 << (ipos - 1)) | (1 << (jpos - 1)))


def zero_bits(number, m):
    # last m bits transform in zeros
    return (number >> m) << m


def splice_bits(number: int, i: int) -> int:
    length = number.bit_length()
    return (number >> (length - i) << i) | (number & ((1 << i) - 1))


def get_middle_bits(number: int, i: int) -> int:
    length = number.bit_length()
    return (number >> i) & ((1 << (length - (i << 1))) - 1)


def change_bytes_order(number: int, order: list) -> int:
    """
    Return number with changed bytes in input `order`
    order - [1, 3, 2, 4] (left to right)
    """
    number_bytes = []
    for _ in range(4):
        b = number & ((1 << 8) - 1)
        print(bin(b))
        number_bytes.append(number & ((1 << 8) - 1))
        number = number >> 8

    new_number = 0
    # байты собираются с конца в начало
    for i, index in enumerate(reversed(order)):
        index -= 1
        new_number |= number_bytes[index] << (i * 8)

    return new_number


def max_div_pow2(number):
    return int(math.log2(number & -number))


def within_range(number: int) -> int:
    #
    p = 0
    while number > 0:
        number >>= 1
        p += 1

    return p - 1


def xor_all_bits(number, p):
    #
    while p > 1:
        number = (number >> (p >> 1)) ^ (number & ((1 << (p >> 1)) - 1))
        p >>= 1

    return number


def transpose_bits(number, arr):
    #
    res = 0
    i = 0
    for item in reversed(arr):
        res |= get_bit_k_pos(number, item) << i
        i += 1

    return res


def cycle_shift_left(number, p, n):
    #
    p = p % n
    return ((number << p) | (number >> (n - p))) & ((1 << n) - 1)


def cycle_shift_right(number, p, n):
    #
    p = p % n
    return (number >> p) | ((number & (1 << p) - 1) << (n - p))


if __name__ == "__main__":
    print(get_bit_k_pos(2, 1))
