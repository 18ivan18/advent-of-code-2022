#!/usr/bin/env python3

import math
from sys import stdin
from typing import List, Set, Tuple


def abs_ceil(num: int):
    if num < 0:
        return math.floor(num)
    return math.ceil(num)


start = (0, 0)


class Knot():
    def __init__(self, x: int, y: int, id: int):
        self.x = x
        self.y = y
        self.visited: Set[Tuple[int, int]] = {(x, y)}
        self.id = 'H' if id == 0 else id

    def visit(self):
        self.visited.add((self.x, self.y))

    def move(self, direction: str):
        if direction == 'R':
            self.y += 1
        if direction == 'L':
            self.y -= 1
        if direction == 'U':
            self.x -= 1
        if direction == 'D':
            self.x += 1
        self.visit()

    def follow(self, other):
        if abs(self.x - other.x) > 1 or abs(self.y - other.y) > 1:
            self.x += abs_ceil((other.x - self.x)/2)
            self.y += abs_ceil((other.y - self.y)/2)
        self.visit()


def print_grid(knots: List[Knot]):
    max_x, max_y, min_x, min_y = 0, 0, 0, 0
    for knot in knots:
        for x, y in knot.visited:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
    for i in range(min_x - 2, max_x+2):
        for j in range(min_y-2, max_y+2):
            for knot in knots:
                if knot.x == i and knot.y == j:
                    print(knot.id, end='')
                    break
            else:
                if (i, j) == start:
                    print('s', end='')
                    continue
                if (i, j) in knots[-1].visited:
                    print('#', end='')
                    continue
                print('.', end='')
        print()
    print()


def solve(input: List[str], number_of_knots: int) -> int:
    knots = [Knot(*start, id) for id in range(number_of_knots)]
    head, *_, tail = knots
    for instruction in input:
        direction, moves = instruction.split(' ')
        for _ in range(int(moves)):
            head.move(direction)
            for prev, next in zip(knots[:-1], knots[1:]):
                next.follow(prev)
            # print_grid(knots)

    return len(tail.visited)


if __name__ == '__main__':
    input = stdin.read().strip().splitlines()
    print(solve(input, 2))
    print(solve(input, 10))
