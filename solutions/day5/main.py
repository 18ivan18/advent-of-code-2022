#!/usr/bin/env python3
from copy import deepcopy
import re
from sys import stdin
from typing import List


def transpose(matrix: List[List]):
    return [[matrix[j][i]
             for j in range(len(matrix))] for i in range(len(matrix[0]))]


def move_boxes(stacks, commands, cratemover9001: bool):
    stacks = deepcopy(stacks)
    for command in commands:
        amount, start, end = command
        selected = stacks[start-1][-amount:]
        if not cratemover9001:
            selected = selected[::-1]
        stacks[end-1] += selected
        del stacks[start-1][-amount:]
    return ''.join([x[-1] for x in stacks])


def solve():
    stacks_input, commands = stdin.read().split('\n\n')
    stacks_input = stacks_input.splitlines(keepends=True)[:-1]
    group_size = 4
    # get every char on index 1 in groups of 4
    # reversing the input because we are working with stacks
    # transpose because we are working with columns rathar than rows
    stacks = transpose([[input[i*group_size + 1] for i in range(len(input) // group_size)]
                       for input in stacks_input[::-1]])
    # filter for empty string
    stacks = [[y for y in x if y != ' '] for x in stacks]

    commands = [list(map(int, re.split(r"\W+", command)[1::2]))
                for command in commands.splitlines()]

    print(move_boxes(stacks, commands, cratemover9001=False))
    print(move_boxes(stacks, commands, cratemover9001=True))


if __name__ == '__main__':
    solve()
