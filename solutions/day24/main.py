#!/usr/bin/env python3

import math
from typing import Dict, List, Set


def lcm(a, b):
    return int(a * b / math.gcd(a, b))


direction_to_coords = {'<': (0, -1), '>': (0, 1), 'v': (1, 0), '^': (-1, 0)}


def bfs(start, end, blizzards, blizzards_repeat_after, pathway, starting_time=1):
    h, l = len(pathway), len(pathway[0])
    q = [(start, starting_time)]

    visited = {(start, starting_time)}
    while q:
        pos, time = q.pop(0)
        x, y = pos
        b = blizzards[time % blizzards_repeat_after]
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)):
            nx, ny = x+dx, y+dy
            if (nx, ny) == end:
                return time
            if 0 < nx < h-1 and 0 < ny < l-1 and (nx, ny, '>') not in b and (nx, ny, '<') not in b and (nx, ny, 'v') not in b and (nx, ny, '^') not in b or (nx, ny) == (0, 1):
                if ((nx, ny), time+1) not in visited:
                    q.append(((nx, ny), time+1))
                    visited.add(((nx, ny), time+1))


def solve():
    pathway = [list(x) for x in open(0).read().strip().splitlines()]
    h, l = len(pathway), len(pathway[0])
    size_x, size_y = h-2, l-2
    start, goal = (0, pathway[0].index(
        '.')), (h-1, pathway[-1].index('.'))
    blizzards_repeat_after = lcm(size_x, size_y)
    blizzards: List[Set] = []
    d = {(i, j, pathway[i][j]) for i in range(1, h)
         for j in range(1, l) if pathway[i][j] in '<>v^'}
    blizzards.append(d)
    for _ in range(blizzards_repeat_after-1):
        b = blizzards[-1]
        d = set()
        for x, y, direction in b:
            dx, dy = direction_to_coords[direction]
            # 0->4, 1->1, 2->2,3->3,4->4,5->1
            nx, ny = ((dx+x-1) % size_x)+1, ((dy+y-1) % size_y)+1
            d.add((nx, ny, direction))
        blizzards.append(d)

    first_trip = bfs(start, goal,
                     blizzards, blizzards_repeat_after, pathway)
    second_trip = bfs(goal, start,
                      blizzards, blizzards_repeat_after, pathway, starting_time=first_trip)

    third_trip = bfs(start, goal,
                     blizzards, blizzards_repeat_after, pathway, starting_time=first_trip+second_trip)
    return first_trip, sum([first_trip, second_trip, third_trip])


if __name__ == '__main__':
    print(solve())
