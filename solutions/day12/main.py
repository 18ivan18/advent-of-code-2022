#!/usr/bin/env python3

from sys import stdin


def find_best_signal():
    pass


def solve() -> None:
    input = [list(x) for x in stdin.read().strip().splitlines()]
    max_x, max_y = len(input), len(input[0])
    start, end = [[(x, y) for y in range(max_y)
                   for x in range(max_x) if input[x][y] == c][0] for c in 'SE']
    input[start[0]][start[1]] = "a"
    input[end[0]][end[1]] = "z"

    q = [(0, end)]
    seen = set()
    p1 = p2 = 0
    while True:
        l, p = q.pop(0)
        if p in seen:
            continue
        seen.add(p)
        x, y = p
        if input[x][y] == "a":
            if not p2:
                p2 = l
            elif p == start:
                p1 = l
                break

        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < max_x and 0 <= ny < max_y and (nx, ny) not in seen and (ord(input[x][y]) - ord(input[nx][ny])) <= 1:
                q.append((l + 1, (nx, ny)))

    print(p1, p2)


if __name__ == '__main__':
    solve()
