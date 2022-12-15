#!/usr/bin/env python3

from sys import stdin
from typing import Iterable, List, Optional, Set, Tuple


def pprint(x): return print(x, end='')


class Point:
    def __init__(self, init_str: str):
        self.y, self.x = map(int, init_str.split(','))

    def __str__(self) -> str:
        return f"{self.x},{self.y}"


class Cave:
    def __init__(self, falling_rocks: int = 500, floor: Optional[int] = None, input_lines: List[str] = []):
        self.sand: Set[Tuple[int, int]] = set()
        self.rocks: Set[Tuple[int, int]] = set()
        self.max_x, self.max_y, self.min_x, self.min_y = 0, 0, 0, float('inf')
        self.floor = floor
        self.falling_rocks = falling_rocks
        self.cnt = 0
        for line in input_lines:
            points = map(Point, line.split(' -> '))
            self.populate(points)
        if floor:
            self.max_x += floor

    def add_rock(self, rock: Tuple[int, int]):
        self.rocks.add((rock[0], rock[1]))
        self.min_x = min(self.min_x, rock[0])
        self.min_y = min(self.min_y, rock[1])
        self.max_x = max(self.max_x, rock[0])
        self.max_y = max(self.max_y, rock[1])

    def add_sand(self, sand: Tuple[int, int]):
        self.sand.add((sand[0], sand[1]))
        if self.floor:
            self.min_y = min(self.min_y, sand[1])
            self.max_y = max(self.max_y, sand[1])

    def visited(self, x: int, y: int):
        if self.floor and x == self.max_x:
            return True
        return (x, y) in self.sand or (x, y) in self.rocks

    def populate(self, points: Iterable[Point]):
        first, *rest = points
        for p in rest:
            min_x, max_x = min(first.x, p.x), max(first.x, p.x)
            min_y, max_y = min(first.y, p.y), max(first.y, p.y)
            if first.x == p.x:
                for i in range(min_y, max_y+1):
                    self.add_rock((first.x, i))
            else:
                for i in range(min_x, max_x+1):
                    self.add_rock((i, first.y))
            first = p

    def print_tile(self, i: int, j: int):
        if i == self.min_x and j == self.falling_rocks:
            pprint('+')
            return
        if self.floor and i == self.max_x or (i, j) in self.rocks:
            pprint('#')
            return
        if (i, j) in self.sand:
            pprint('o')
            return
        pprint('.')

    def print(self):
        for i in range(len(str(max(self.min_x, self.max_x, self.falling_rocks)))):
            pprint('  ')
            for j in range(self.min_y, self.max_y + 1):
                if j in [self.min_y, self.max_y, self.falling_rocks]:
                    pprint(str(j)[i])
                else:
                    pprint(' ')
            print()

        for i in range(self.min_x, self.max_x + 1):
            pprint(f"{i} ")
            for j in range(self.min_y, self.max_y + 1):
                self.print_tile(i, j)
            print()
        print()

    def fall(self, grain_of_sand: List[int]):
        while True:
            if not self.floor and (grain_of_sand[0] >= self.max_x or not (self.min_y <= grain_of_sand[1] <= self.max_y)):
                return False
            if self.visited(grain_of_sand[0] + 1, grain_of_sand[1]):
                if self.visited(grain_of_sand[0] + 1, grain_of_sand[1]-1):
                    if self.visited(grain_of_sand[0]+1, grain_of_sand[1]+1):
                        break
                    else:
                        grain_of_sand[1] += 1
                else:
                    grain_of_sand[1] -= 1
            else:
                grain_of_sand[0] += 1

        if self.floor and self.visited(0, self.falling_rocks):
            return False
        self.add_sand((grain_of_sand[0], grain_of_sand[1]))
        return True

    def get_new_sand_grain(self):
        return [self.min_x, self.falling_rocks]

    def solve(self):
        while True:
            sand_grain = self.get_new_sand_grain()
            if not self.fall(sand_grain):
                break
            self.cnt += 1
        self.print()
        print(self.cnt)


def solve(input: List[str], floor: Optional[int] = None):
    cave = Cave(floor=floor, input_lines=input)
    cave.solve()


if __name__ == '__main__':
    input = stdin.read().strip().splitlines()
    solve(input)
    solve(input, floor=2)
