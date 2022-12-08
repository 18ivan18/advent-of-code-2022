#!/usr/bin/env python3

from itertools import product
from sys import stdin


def solve():
    input = stdin.read().splitlines()
    size = len(input)
    number_of_visible, max_scenic_score = 0, 0
    for i, j in product(range(size), range(size)):
        scenic_score, visible = 1, False
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            n, compare_idx_i, compare_idx_j = 0, i+di, j+dj
            while 0 <= compare_idx_i < size and 0 <= compare_idx_j < size:
                n += 1
                if input[compare_idx_i][compare_idx_j] >= input[i][j]:
                    break
                compare_idx_i, compare_idx_j = compare_idx_i + di, compare_idx_j + dj
            else:
                visible = True
            scenic_score *= n
        number_of_visible, max_scenic_score = number_of_visible + \
            visible, max(max_scenic_score, scenic_score)

    print(number_of_visible, max_scenic_score)


if __name__ == '__main__':
    solve()
