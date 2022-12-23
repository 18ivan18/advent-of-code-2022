#!/usr/bin/env python3

def get_pos(dir: str, x: int, y: int):
    if dir == 'N':
        return x-1, y
    if dir == 'S':
        return x+1, y
    if dir == 'E':
        return x, y+1
    if dir == 'W':
        return x, y-1
    if dir == 'NE':
        return x-1, y+1
    if dir == 'NW':
        return x-1, y-1
    if dir == 'SE':
        return x+1, y+1
    if dir == 'SW':
        return x+1, y-1
    raise ValueError


def print_map(min_x, max_x, min_y, max_y, elves):
    for i in range(min_x, max_x+1):
        for j in range(min_y, max_y+1):
            print('#' if (i, j) in elves else '.', end='')
        print()
    print()


list_of_dirs = [
    (lambda elf, elves: get_pos(
        'N', *elf) not in elves and get_pos('NE', *elf) not in elves and get_pos('NW', *elf) not in elves, 'N'),
    (lambda elf, elves: get_pos('S', *elf) not in elves and get_pos(
        'SE', *elf) not in elves and get_pos('SW', *elf) not in elves, 'S'),
    (lambda elf, elves: get_pos('W', *elf) not in elves and get_pos(
        'NW', *elf) not in elves and get_pos('SW', *elf) not in elves, 'W'),
    (lambda elf, elves: get_pos('E', *elf) not in elves and get_pos('NE', *elf) not in elves and get_pos('SE', *elf) not in elves, 'E')]


def has_any_neighbours(elf, elves):
    for dir in ('N', 'S', 'E', 'W', 'NE', 'NW', 'SE', 'SW'):
        if get_pos(dir, *elf) in elves:
            return True
    return False


def solve(rounds=10):
    input = [list(x) for x in open(0).read().strip().splitlines()]
    elves = {(i, j) for j in range(len(input[0]))
             for i in range(len(input)) if input[i][j] == '#'}
    min_x, max_x, min_y, max_y = 0, len(input), 0, len(input[0])
    print_map(min_x, max_x, min_y, max_y, elves)
    part_1, part_2, moved = 0, 1, True
    while moved:
        # first round
        proposals = {}
        for elf in elves:
            if not has_any_neighbours(elf, elves):
                proposals[elf] = elf
                continue
            for pred, dir in list_of_dirs:
                if pred(elf, elves):
                    proposals[elf] = get_pos(dir, *elf)
                    break
            else:
                proposals[elf] = elf
        list_of_dirs.append(list_of_dirs.pop(0))
        # second round
        new_pos = {new_pos if list(proposals.values()).count(
            new_pos) == 1 else old_pos for old_pos, new_pos in proposals.items()}
        if elves == new_pos:
            moved = False
        elves = new_pos
        sort_by_x, sort_by_y = sorted(elves), sorted(elves, key=lambda x: x[1])
        min_x, max_x, min_y, max_y = sort_by_x[0][0], sort_by_x[-1][0], sort_by_y[0][1], sort_by_y[-1][1]
        # print(f"ROUND {part_2}")
        # print_map(min_x, max_x, min_y, max_y, elves)

        if part_2 == rounds:
            # result
            for i in range(min_x, max_x+1):
                for j in range(min_y, max_y+1):
                    part_1 += 0 if (i, j) in elves else 1
        part_2 += moved

    return part_1, part_2


if __name__ == '__main__':
    print(solve(rounds=10))
