#!/usr/bin/env python3

from copy import deepcopy
import re
from typing import List

direction_to_coords = {0: (0, 1, '>'), 1: (
    1, 0, 'V'), 2: (0, -1, '<'), 3: (-1, 0, '^')}


def walk(maze: List[List[str]], instructions: List[str]):
    """
    0 - right (>)
    1 - down (V)
    2 - left (<)
    3 - up (^)

    turning R - 90 deg clockwise (+1)
    turning L - 90 deg counterclockwise (-1)
    """
    with_movement = deepcopy(maze)
    x, y, direction = 0, maze[0].index('.'), 0
    for instruction in instructions:
        try:
            steps = int(instruction)
            for _ in range(steps):
                dx, dy, d = direction_to_coords[direction]
                new_x, new_y = (x+dx) % len(maze), (y+dy) % len(maze[x])
                while maze[new_x][new_y] == ' ':
                    new_x, new_y = (new_x+dx) % len(maze), (new_y +
                                                            dy) % len(maze[new_x])
                if maze[new_x][new_y] == '#':
                    break
                with_movement[x][y] = d
                x, y = new_x, new_y
        except:
            if instruction == 'R':
                direction = (direction + 1) % 4
            elif instruction == 'L':
                direction = (direction-1) % 4
            else:
                raise ValueError

    with_movement[x][y] = 'X'
    for row in with_movement:
        print(''.join(row))

    return x, y, direction


def solution(input):
    maze = [list(x) for x in input[:-2]]
    instructions = re.findall("\d+|\D+", input[-1])
    x, y, direction = walk(maze, instructions)
    print(x, y, direction)
    return (x+1)*1000+(y+1)*4+direction


if __name__ == '__main__':
    input = open(0).read().splitlines()
    print(solution(input))
