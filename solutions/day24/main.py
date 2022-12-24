#!/usr/bin/env python3

import math
from typing import Dict, List, Set


def lcm(a, b):
    return (a / math.gcd(a, b)) * b


direction_to_coords = {'<': (0, -1), '>': (0, 1), 'v': (1, 0), '^': (-1, 0)}


def solve():
    pathway = [list(x) for x in open(0).read().strip().splitlines()]
    h, l = len(pathway), len(pathway[0])
    print(h, l)
    size_x, size_y = h-2, l-2
    start_x, start_y, goal_x, goal_y = 0, pathway[0].index(
        '.'), h-1, pathway[-1].index('.')
    blizzards_repeat_after = int(lcm(size_x, size_y))
    blizzards: List[Set] = []
    d = set()
    for i in range(1, len(pathway)):
        for j in range(1, len(pathway[0])):
            if pathway[i][j] in ['<', '>', 'v', '^']:
                d.add((i, j, pathway[i][j]))
    blizzards.append(d)
    for _ in range(blizzards_repeat_after-1):
        b = blizzards[-1]
        d = set()
        for x, y, direction in b:
            dx, dy = direction_to_coords[direction]
            # 0->4, 1->1, 2->2,3->3,4->4,5->1
            nx, ny = (dx+x), (dy+y)
            if nx > size_x:
                nx %= size_x
            if ny > size_y:
                ny %= size_y
            if nx == 0:
                nx = size_x
            if ny == 0:
                ny = size_y
            d.add((nx, ny, direction))
        blizzards.append(d)
    q = [(start_x, start_y, 1)]
    while q:
        x, y, time = q.pop(0)
        # print(x, y, time)
        b = blizzards[time % blizzards_repeat_after]
        added = False
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx, ny = x+dx, y+dy
            if nx == goal_x and ny == goal_y:
                return time
            if nx > 0 and nx < h-1 and ny > 0 and ny < l-1 and (nx, ny, '>') not in b and (nx, ny, '<') not in b and (nx, ny, 'v') not in b and (nx, ny, '^') not in b:
                added = True
                q.append((nx, ny, time+1))
        if not added:
            q.append((x, y, time+1))
        # print(q)


if __name__ == '__main__':
    print(solve())
