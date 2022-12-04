#!/usr/bin/env python3
from functools import reduce
from sys import stdin
import re


class Range():
    def __init__(self, range_str: str) -> None:
        if not re.match("^\d+-\d+$", range_str):
            raise ValueError(input)
        f, t = range_str.split('-')
        self.f = int(f)
        self.t = int(t)

    def __and__(self, other) -> bool:
        """
        Contains
        """
        return self.f <= other.f and self.t >= other.t or other.f <= self.f and other.t >= self.t

    def __or__(self, other) -> bool:
        """
        Overlaps
        """
        return self.f <= other.f <= self.t or other.f <= self.f <= other.t


def solve():
    input = stdin.read().strip().splitlines()
    containing = reduce(lambda prev, curr: prev +
                        (Range(curr.split(',')[0]) & Range(curr.split(',')[1])), input, 0)
    overlaping = reduce(lambda prev, curr: prev +
                        (Range(curr.split(',')[0]) | Range(curr.split(',')[1])), input, 0)
    return containing, overlaping


if __name__ == '__main__':
    print(*solve())
