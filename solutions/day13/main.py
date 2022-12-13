#!/usr/bin/env python3

from functools import cmp_to_key
import json
from sys import stdin
from typing import List

# >0 if first > second
# 0 if equal
# <0 if first < second


def compare_arrays_lexicographically(first: List, second: List):
    for i in range(min(len(first), len(second))):
        if isinstance(first[i], int) and isinstance(second[i], int) and first[i] != second[i]:
            return first[i] - second[i]
        if isinstance(first[i], int) and isinstance(second[i], list):
            comp = compare_arrays_lexicographically([first[i]], second[i])
            if not comp:
                continue
            return comp
        if isinstance(first[i], list) and isinstance(second[i], int):
            comp = compare_arrays_lexicographically(first[i], [second[i]])
            if not comp:
                continue
            return comp
        if isinstance(first[i], list) and isinstance(second[i], list):
            comp = compare_arrays_lexicographically(first[i], second[i])
            if not comp:
                continue
            return comp

    return len(first) - len(second)


assert(compare_arrays_lexicographically(
    [1, 1, 3, 1, 1], [1, 1, 5, 1, 1]) < 0)

assert(compare_arrays_lexicographically(
    [[1], [2, 3, 4]], [[1], 4]) < 0)

assert(compare_arrays_lexicographically(
    [9], [[8, 7, 6]]) > 0)

assert(compare_arrays_lexicographically(
    [[4, 4], 4, 4], [[4, 4], 4, 4, 4]) < 0)

assert(compare_arrays_lexicographically(
    [7, 7, 7, 7], [7, 7, 7]) > 0)

assert(compare_arrays_lexicographically(
    [], [3]) < 0)

assert(compare_arrays_lexicographically(
    [[[]]], [[]]) > 0)

assert(compare_arrays_lexicographically(
    [1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]) > 0)


def parse(s: str):
    return json.loads(s)


assert(parse('[1, [2, [3, [4, [5, 6, 7]]]], 8, 9]')
       == [1, [2, [3, [4, [5, 6, 7]]]], 8, 9])
assert(parse(
    '[[],[[[1],0],[9,7,7,[3,9,3,9,10]],8,[5,10,[5,5,8,3,7],7,[9,0,7]]],[[8,2,[0],7],4]]') == [[], [[[1], 0], [9, 7, 7, [3, 9, 3, 9, 10]], 8, [5, 10, [5, 5, 8, 3, 7], 7, [9, 0, 7]]], [[8, 2, [0], 7], 4]])


def parse_and_compare(s: str):
    first, second = s.split('\n')
    return compare_arrays_lexicographically(parse(first), parse(second)) <= 0


def solve_part_1(input: str):
    input_lines = input.split('\n\n')
    result = 0
    for i, pair in enumerate(input_lines):
        result += (i+1)*parse_and_compare(pair)
    return result


def solve_part_2(input: str):
    divider_two, divider_six = [[2]], [[6]]
    input_lines = list(map(lambda x: parse(
        x), input.replace('\n\n', '\n').splitlines())) + [divider_two, divider_six]
    s = sorted(input_lines, key=cmp_to_key(compare_arrays_lexicographically))
    print((s.index(divider_two)+1) * (s.index(divider_six)+1))
    for i, array in enumerate(s):
        print(array)


if __name__ == '__main__':
    input = stdin.read()
    print(solve_part_1(input))
    print(solve_part_2(input))
