#!/usr/bin/env python3


rocks = [{(0, 0), (0, 1), (0, 2), (0, 3)},
         {(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)},
         {(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)},
         {(0, 0), (1, 0), (2, 0), (3, 0)},
         {(0, 0), (1, 0), (1, 1), (0, 1)}]


def print_tower(rocks, rock=set()):
    max_x = max(rocks)[0]
    for i in range(max_x, 0, -1):
        print('|', end='')
        for j in range(7):
            print('@' if (i, j) in rock else '#' if (i, j)
                  in rocks else '.', end='')
        print('|')
    print('+-------+\n')


Y_OFFSET = 2
X_OFFSET = 4


def can_move(direction, rock, rocks):
    for x, y in rock:
        if (x, y+direction) in rocks or y+direction not in range(7):
            return False
    return True


def get_height(rock):
    return abs(max(rock)[0] - min(rock)[0])


def get_top_view(rocks):
    maxys = [float('-inf') for _ in range(7)]
    for (x, y) in rocks:
        maxys[y] = max(maxys[y], x)
    v = max(maxys)
    return tuple(m - v for m in maxys)


def solve(directions, iterations=2022):
    # direction id, rock id
    did, rid, height = 0, 0, 0
    solids = {(0, y) for y in range(7)}
    seen, additional = {}, 0
    i = 0
    while i < iterations:
        height += X_OFFSET
        next_rock = {(x+height, y+Y_OFFSET) for x, y in rocks[rid]}
        rid = (rid+1) % len(rocks)
        height += get_height(next_rock)
        while True:
            direction = directions[did]
            did = (did+1) % len(directions)
            if can_move(direction, next_rock, solids):
                next_rock = {(x, y+direction) for x, y in next_rock}
            down = {(x-1, y) for x, y in next_rock}
            if len(solids & down) == 0:
                next_rock = down
                height -= 1
            else:
                break
        i += 1
        solids = solids | next_rock
        height = max(solids)[0]
        topv = get_top_view(solids)
        if (topv, did, rid) in seen:
            old_i, old_height = seen[(topv, did, rid)]
            repeat = (iterations-i)//(i-old_i)
            i += (i-old_i)*repeat
            additional += repeat*(height-old_height)
            seen = {}

        seen[(topv, did, rid)] = (i, height)
    # print_tower(solids)
    # print(height, additional, height+additional)
    print(height+additional)


if __name__ == '__main__':
    directions = [-1 if x == '<' else 1 for x in open(0).read()]
    solve(directions)
    solve(directions, 1_000_000_000_000)
