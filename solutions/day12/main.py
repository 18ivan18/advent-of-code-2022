#!/usr/bin/env python3

from sys import stdin


def solve() -> None:
    input = [list(x) for x in stdin.read().strip().splitlines()]
    max_x, max_y = len(input), len(input[0])
    start, end = [[(x, y) for y in range(max_y)
                   for x in range(max_x) if input[x][y] == c][0] for c in 'SE']
    input[start[0]][start[1]] = "a"
    input[end[0]][end[1]] = "z"

    q = [(0, end)]
    seen = set()
    distance_to_start = distance_to_a = 0
    while True:
        path_len, coords = q.pop(0)
        x, y = coords
        if input[x][y] == "a":
            if not distance_to_a:
                distance_to_a = path_len
            if coords == start:
                distance_to_start = path_len
                break

        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < max_x and 0 <= ny < max_y and (nx, ny) not in seen and (ord(input[x][y]) - ord(input[nx][ny])) <= 1:
                q.append((path_len + 1, (nx, ny)))
                seen.add((nx, ny))

    print(distance_to_start, distance_to_a)


if __name__ == '__main__':
    solve()
