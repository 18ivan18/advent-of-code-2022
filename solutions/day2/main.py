#!/usr/bin/env python3
from sys import stdin

strategy_solution = {'A X': 4,
                     'A Y': 8,
                     'A Z': 3,
                     'B X': 1,
                     'B Y': 5,
                     'B Z': 9,
                     'C X': 7,
                     'C Y': 2,
                     'C Z': 6, }


strategy_solution_part2 = {'A X': 3,  # rock wins -> rock vs scissors = A Z
                           'A Y': 4,  # rock draws -> rock vs rock = A X
                           'A Z': 8,  # A Y
                           'B X': 1,  # paper winds -> paper vs rock = B X
                           'B Y': 5,  # paper draws -> paper vs paper = B Y
                           'B Z': 9,  # B Z
                           'C X': 2,  # scissors wins -> scissors vs paper = C Y
                           'C Y': 6,  # scissors draws -> C Z
                           'C Z': 7, }  # C X


def solve() -> None:
    input = list(
        map(lambda x: strategy_solution_part2[x], stdin.read().split('\n')))
    print(sum(input))


if __name__ == '__main__':
    solve()
