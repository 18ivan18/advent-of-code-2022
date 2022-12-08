#!/usr/bin/env python3

from functools import reduce
from sys import stdin


def look_at(seen, row):
    j, size, max = 0, len(row), -1
    while j < size and max != 9:
        if row[j] > max:
            seen[j] = True
            max = row[j]
        j += 1

    j, max = size-1, -1
    while j >= 0 and max != 9:
        if row[j] > max:
            seen[j] = True
            max = row[j]
        j -= 1

    return seen


def look_at_col(seen, input, i):
    j, size, max = 0, len(input), -1
    while j < size and max != 9:
        if input[j][i] > max:
            seen[j][i] = True
            max = input[j][i]
        j += 1

    j, max = size-1, -1
    while j >= 0 and max != 9:
        if input[j][i] > max:
            seen[j][i] = True
            max = input[j][i]
        j -= 1

    return seen


def get_scenic_score(input, i, j):
    size = len(input)
    indx_top = 0 if i == 0 or i == size-1 else 1
    indx_bottom = 0 if i == 0 or i == size-1 else 1
    indx_right = 0 if j == 0 or j == size-1 else 1
    indx_left = 0 if j == 0 or j == size-1 else 1
    while i + indx_bottom < size - 1 and input[i][j] > input[i+indx_bottom][j]:
        indx_bottom += 1
    while i - indx_top > 0 and input[i][j] > input[i-indx_top][j]:
        indx_top += 1
    while j + indx_right < size - 1 and input[i][j] > input[i][j+indx_right]:
        indx_right += 1
    while j - indx_left > 0 and input[i][j] > input[i][j - indx_left]:
        indx_left += 1
    return indx_right*indx_bottom*indx_left*indx_top


def solve():
    input = [[int(y) for y in x] for x in stdin.read().splitlines()]
    seen = [[False for _ in y] for y in input]
    size = len(input)
    for i in range(size):
        look_at(seen[i], input[i])
        look_at_col(seen, input, i)
    max,  i_max, j_max = 0, 0, 0
    for i in range(size):
        for j in range(size):
            sc = get_scenic_score(input, i, j)
            if(sc > max):
                max = sc
                i_max = i
                j_max = j
    print(reduce(lambda curr, prev: curr+prev.count(True), seen, 0))
    print(max, i_max, j_max)


if __name__ == '__main__':
    solve()
