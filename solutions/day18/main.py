#!/usr/bin/env python3

from functools import reduce
from sys import stdin
from typing import List


class Cube:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x, self.y, self.z = x, y, z
        # 0:x-1,1:x+1,2:y-1,3:y+1,4:z-1,5:z+1
        self.sides = [True for x in range(6)]

    def place_next_to(self, other):
        if self.x == other.x-1 and self.y == other.y and self.z == other.z:
            self.sides[0] = False
        if self.x == other.x+1 and self.y == other.y and self.z == other.z:
            self.sides[1] = False
        if self.y == other.y-1 and self.x == other.x and self.z == other.z:
            self.sides[2] = False
        if self.y == other.y+1 and self.x == other.x and self.z == other.z:
            self.sides[3] = False
        if self.z == other.z+1 and self.x == other.x and self.y == other.y:
            self.sides[4] = False
        if self.z == other.z+1 and self.x == other.x and self.y == other.y:
            self.sides[5] = False

    def sides_open(self):
        return self.sides.count(True)


def solve():
    input = [list(map(int, x.split(',')))
             for x in stdin.read().strip().splitlines()]
    cubes: List[Cube] = []
    # O(n^2)

    for x, y, z in input:
        c = Cube(x, y, z)
        for cube in cubes:
            c.place_next_to(cube)
            cube.place_next_to(c)
        cubes.append(c)

    part_1 = reduce(lambda curr, next: curr+next.sides_open(), cubes, 0)
    print(part_1)


if __name__ == '__main__':
    solve()
