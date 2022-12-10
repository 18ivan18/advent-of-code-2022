#!/usr/bin/env python3

from functools import reduce
from sys import stdin
from typing import List


def solve() -> None:
    input = stdin.read().strip().splitlines()
    x, cycle, signal_strength = 1, 1, 0

    def create_command_list(command):
        if command == 'noop':
            return [command]
        return ['noop', command]
    commands: List[str] = reduce(lambda curr, next: [
        *curr, *create_command_list(next)], input, [])

    for command in commands:
        print('#' if (cycle-1) % 40 in range(x-1, x+2) else '.', end='')
        if cycle % 40 == 0:
            print()
        if cycle % 40 == 20:
            signal_strength += x*cycle
            # print(x*cycle, cycle, x)
        cycle += 1
        if command == 'noop':
            continue
        _, value = command.split(' ')
        x += int(value)

    print(signal_strength)


if __name__ == '__main__':
    solve()
