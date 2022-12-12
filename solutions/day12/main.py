#!/usr/bin/env python3

from collections import deque
from copy import deepcopy
from itertools import product
from sys import stdin
from typing import List


def find_best_signal(input: List[List[str]], curr_x: int, curr_y: int, end_x: int, end_y: int, path_len: int = 0, paths=[]):
    max_x, max_y, curr_value = len(input), len(input[0]), input[curr_x][curr_y]
    for dx, dy, direction in ((0, 1, '>'), (0, -1, '<'), (1, 0, 'V'), (-1, 0, '^')):
        if 0 <= curr_x+dx < max_x and 0 <= curr_y+dy < max_y and (ord(curr_value) - ord(input[curr_x+dx][curr_y+dy])) >= -1 and input[curr_x+dx][curr_y+dy] not in ['>', '<', '^', 'V']:
            input[curr_x][curr_y] = direction
            if curr_x+dx == end_x and curr_y+dy == end_y:
                # for x in input:
                #     print(x)
                # print()
                paths.append((path_len+1, deepcopy(input)))
                input[curr_x][curr_y] = curr_value
                continue
            find_best_signal(input, curr_x+dx, curr_y+dy, end_x, end_y,
                             path_len=path_len+1, paths=paths)
            input[curr_x][curr_y] = curr_value


def solve() -> None:
    input = [list(x) for x in stdin.read().strip().splitlines()]
    for i, j in product(range(len(input)), range(len(input[0]))):
        if input[i][j] == 'S':
            input[i][j] = 'a'
            start = i, j
        if input[i][j] == 'E':
            input[i][j] = 'z'
            end = i, j

    paths = []
    find_best_signal(input, *start, *end, paths=paths)
    m, p = min(paths)
    print(m)
    for x in p:
        print(x)


if __name__ == '__main__':
    solve()
