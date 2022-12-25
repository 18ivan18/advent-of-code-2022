#!/usr/bin/env python3


from collections import deque


SNAFU_to_digit = {'1': 1, '2': 2, '0': 0, '-': -1, '=': -2}
digit_to_SNAFU = {y: x for x, y in SNAFU_to_digit.items()}
base = 5


def SNAFU_to_decimal(snafu_number):
    snafu = 0
    for i, s in enumerate(snafu_number[::-1]):
        snafu += SNAFU_to_digit[s] * (base**i)
    return snafu


# 4890 % 5 = 0 -> 0
# 978 % 5 = 3 -> 3 - 5 = -2 -> = && (978+5)//5
# 196 % 5 = 1
# 39 % 5 = 4 -> 4 - 5 = -1 -> - && (39+5)//5
# 8 % 5 = 3 -> 3 - 5 = -2 -> = && (8+5)//5
# 2 % 5 = 2
def decimal_to_snafu(decimal):
    snafu = deque()
    while decimal:
        d = decimal % base
        if d > 2:
            d = d-base
            decimal += base
        decimal //= base
        snafu.appendleft(digit_to_SNAFU[d])
    return ''.join(snafu)


def solve():
    numbers = open(0).read().strip().splitlines()
    return decimal_to_snafu(sum(map(SNAFU_to_decimal, numbers)))


if __name__ == '__main__':
    print(solve())
