#!/usr/bin/env python3

import math
from sys import stdin
from typing import Set, Tuple


def abs_ceil(num: int):
    if num < 0:
        return math.floor(num)
    return math.ceil(num)


class Knot():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.visited: Set[Tuple[int, int]] = {(x, y)}

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


def print_grid(head, tail):
    for i in range(-5, 1):
        for j in range(7):
            if head.x == i and head.y == j:
                print('H', end='')
                continue
            if tail.x == i and tail.y == j:
                print('T', end='')
                continue
            if (i, j) in tail.visited:
                print('#', end='')
                continue
            else:
                print('.', end='')
        print()
    print()


def solve() -> None:
    # number_of_knots = 2
    number_of_knots = 10
    knots = [Knot(0, 0) for _ in range(number_of_knots)]
    head, *_, tail = knots
    input = stdin.read().strip().splitlines()
    for instruction in input:
        direction, moves = instruction.split(' ')
        for _ in range(int(moves)):
            head.move(direction)
            for prev, next in zip(knots[:-1], knots[1:]):
                next.follow(prev)
            # print_grid(head, tail)

    print(len(tail.visited))


if __name__ == '__main__':
    solve()
