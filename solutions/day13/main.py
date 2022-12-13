#!/usr/bin/env python3

from functools import cmp_to_key
from sys import stdin
from typing import List


def compare_arrays_lexicographically(first: List, second: List):
    """
    - >0 if first > second
    - 0 if equal
    - <0 if first < second
    """
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


def solve_part_1(input: str):
    input_lines = input.split('\n\n')
    result = 0
    for i, pair in enumerate(input_lines):
        first, second = pair.split('\n')
        result += (i+1)*(compare_arrays_lexicographically(eval(first),
                                                          eval(second)) <= 0)
    return result


def solve_part_2(input: str):
    divider_two, divider_six = [[2]], [[6]]
    input_lines = list(map(lambda x: eval(
        x), input.replace('\n\n', '\n').splitlines())) + [divider_two, divider_six]
    s = sorted(input_lines, key=cmp_to_key(compare_arrays_lexicographically))
    return (s.index(divider_two)+1) * (s.index(divider_six)+1)
    # for array in s:
    #     print(array)


if __name__ == '__main__':
    input = stdin.read()
    print(solve_part_1(input))
    print(solve_part_2(input))
