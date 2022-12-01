#!/usr/bin/env python3
from typing import List
from sys import stdin


def solve() -> None:
    input = stdin.read()

    calories: List[int] = sorted(map(lambda x: sum(map(int, x.split('\n'))),
                                     input.split('\n\n')), reverse=True)
    print(calories[0])
    print(sum(calories[:3]))


if __name__ == '__main__':
    solve()
