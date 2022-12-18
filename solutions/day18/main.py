#!/usr/bin/env python3

from sys import stdin
from typing import List, Tuple


def neighbours(point: Tuple[int, int, int], min: int, max: int):
    neighbours = set()
    x, y, z = point
    for dx, dy, dz in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
        if min <= x <= max and min <= y <= max and min <= z <= max:
            neighbours.add((x+dx, y+dy, z+dz))
    return neighbours


def solve():
    input = {tuple(int(y) for y in x.split(','))
             for x in stdin.read().strip().splitlines()}
    min_coord = min(min(point) for point in input) - 1
    max_coord = max(max(point) for point in input) + 1
    part_1 = 0
    for point in input:
        part_1 += 6 - len(neighbours(point, min_coord, max_coord) & input)
    print(part_1)

    part_2 = 0
    # BFS from the outside, not the inside :facepalm:
    q = [(min_coord, min_coord, min_coord)]
    steam = {q[0]}
    while q:
        point = q.pop()
        for other in neighbours(point, min_coord, max_coord) - steam:
            if other in input:
                part_2 += 1
            else:
                steam.add(other)
                q.append(other)
    print(part_2)


if __name__ == '__main__':
    solve()
