#!/usr/bin/env python3

from sys import stdin
from typing import List, Optional, Set, Tuple

rocks: Set[Tuple[int, int]] = set()
sand: Set[Tuple[int, int]] = set()


def pprint(x): return print(x, end='')


class Point:
    def __init__(self, init_str: str):
        self.x, self.y = map(int, init_str.split(','))

    def __str__(self) -> str:
        return f"{self.x},{self.y}"

    def rocks_falling(self, other):
        min_x, max_x = min(self.x, other.x), max(self.x, other.x)
        min_y, max_y = min(self.y, other.y), max(self.y, other.y)
        if self.x == other.x:
            for i in range(min_y, max_y+1):
                rocks.add((self.x, i))
            return
        for i in range(min_x, max_x+1):
            rocks.add((i, self.y))


def print_map(rocks: Set[Tuple[int, int]], min_x: int = 0, max_x: int = 0, min_y: int = 0, max_y: int = 0, falling_rocks: int = 500, floor: Optional[int] = None):
    for i in range(len(str(max(min_x, max_x, falling_rocks)))):
        pprint('  ')
        for j in range(min_y, max_y + 1):
            if j in [min_y, max_y, falling_rocks]:
                pprint(str(j)[i])
            else:
                pprint(' ')
        print()

    for i in range(min_x, max_x + 1):
        pprint(f"{i} ")
        for j in range(min_y, max_y + 1):
            if i == min_x and j == falling_rocks:
                pprint('+')
                continue
            if floor and i == max_x:
                pprint('#')
                continue
            pprint('#' if (j, i) in rocks else 'o' if (j, i) in sand else '.')
        print()
    print()


def visited(x, y, max_x: int = 0, floor: Optional[int] = None):
    if floor and y == max_x:
        return True
    return (x, y) in sand or (x, y) in rocks


def fall(grain_of_sand: List[int], min_x: int = 0, max_x: int = 0, max_y: int = 0, floor: Optional[int] = None):
    while True:
        if visited(grain_of_sand[0], grain_of_sand[1]+1, floor=floor, max_x=max_x):
            if visited(grain_of_sand[0] - 1, grain_of_sand[1]+1, floor=floor, max_x=max_x):
                if visited(grain_of_sand[0]+1, grain_of_sand[1]+1, floor=floor, max_x=max_x):
                    break
                else:
                    grain_of_sand[0] += 1
            else:
                grain_of_sand[0] -= 1
        else:
            grain_of_sand[1] += 1

    if visited(500, 0):
        return False
    sand.add((grain_of_sand[0], grain_of_sand[1]))
    return True


def find_edges(rocks: Set[Tuple[int, int]]):
    max_x, max_y, min_x, min_y = 0, 0, 0, float('inf')
    for rock in rocks:
        y, x = rock
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    return min_x, min_y, max_x, max_y


def solve(input: List[str], floor: Optional[int] = None):
    falling_rocks = 500
    for line in input:
        first, *rest = map(Point, line.split(' -> '))
        for p in rest:
            first.rocks_falling(p)
            first = p
    min_x, min_y, max_x, max_y = find_edges(rocks)
    if floor:
        max_x += floor
    cnt = 0
    while True:
        sand_grain = [falling_rocks, min_x]
        if not fall(sand_grain, min_x=min_x, max_x=max_x, max_y=max_y, floor=floor):
            break
        cnt += 1
    min_x, min_y, max_x, max_y = find_edges(rocks | sand)
    print_map(rocks, min_x=min_x, max_x=max_x, min_y=min_y,
              max_y=max_y, falling_rocks=falling_rocks, floor=floor)
    print(cnt)


if __name__ == '__main__':
    input = stdin.read().strip().splitlines()
    # solve(input)
    solve(input, floor=2)
