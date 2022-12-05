#!/usr/bin/env python3
from copy import deepcopy
import re
from sys import stdin
from typing import List


def transpose(matrix: List[List]):
    return [[matrix[j][i]
             for j in range(len(matrix))] for i in range(len(matrix[0]))]


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

    stacks_part2 = deepcopy(stacks)

    for command in commands.splitlines():
        split_command = re.split(r"\W+", command)
        move, _from, to = list(map(int, split_command[1::2]))
        for i in range(move):
            stacks[to - 1].append(stacks[_from - 1].pop())
            stacks_part2[to - 1].append(stacks_part2[_from - 1][-(move-i)])
        stacks_part2[_from - 1] = stacks_part2[_from - 1][:-move]

    return (''.join([x[-1] for x in stacks]), ''.join([x[-1] for x in stacks_part2]))


if __name__ == '__main__':
    print(*solve())
