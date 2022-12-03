#!/usr/bin/env python3
from sys import stdin
from typing import List


def to_priority(s: str) -> int:
    return ord(s) - ord('a') + 1 + (ord('a') - ord('A') + 26) * s.isupper()


def common_letter(s: str) -> str:
    half = len(s) // 2
    return (set(s[:half]) & set(s[half:])).pop()


def split_into_groups(x: List, n: int):
    return zip(*(iter(x),) * n)


def solve() -> None:
    input = stdin.read().strip().splitlines()
    print(sum(map(to_priority, map(common_letter, input))))

    groups_of_three = split_into_groups(input, 3)
    print(sum(map(to_priority, ([(set(g[0]) & set(g[1]) & set(g[2])).pop()
          for g in groups_of_three]))))


if __name__ == '__main__':
    solve()
