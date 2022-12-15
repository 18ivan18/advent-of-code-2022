#!/usr/bin/env python3

import re
from typing import List, Tuple
from z3 import Int, Solver, Abs


def manhattan(p1: Tuple[int, int], p2: Tuple[int, int]):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def solve(input_file_name: str, y: int = 10):
    with open(input_file_name) as f:
        input = f.read().strip().splitlines()
    sensors = [list(map(int, re.findall('-?\d+', x)))
               for x in input]
    intervals: List[Tuple[int, int]] = []
    known = set()
    for sx, sy, bx, by in sensors:
        distance = manhattan((sx, sy), (bx, by))
        dist_to_targ = abs(sy - y)
        dist_left = distance - dist_to_targ
        if dist_left < 0:
            continue
        intervals.append((sx-dist_left, sx+dist_left))

        if by == y:
            known.add(bx)

    q: List[List[int]] = []
    for lo, hi in sorted(intervals):
        if not q:
            q.append([lo, hi])
            continue
        _, qhi = q[-1]
        if lo > qhi > +1:
            q.append([lo, hi])
            continue
        q[-1][1] = max(qhi, hi)

    cannot = set()
    for lo, hi in q:
        for x in range(lo, hi + 1):
            cannot.add(x)

    print(len(cannot - known))


def solve_part_2(input_file_name: str):
    with open(input_file_name) as f:
        input = f.read().strip().splitlines()
    sensors = [list(map(int, re.findall('-?\d+', x)))
               for x in input]
    s = Solver()
    x, y = Int("x"), Int("y")
    s.add(x >= 0, x <= 4000000, y >= 0, y <= 4000000)
    for sx, sy, bx, by in sensors:
        dist = manhattan((sx, sy), (bx, by))
        s.add(Abs(x - sx) + Abs(y - sy) > dist)
    s.check()
    model = s.model()
    print(model[x].as_long() * 4000000 + model[y].as_long())


if __name__ == '__main__':
    solve('inputExample.txt', y=10)
    solve('input.txt', y=2000000)
    solve_part_2('inputExample.txt')
    solve_part_2('input.txt')
