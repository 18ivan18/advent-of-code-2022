#!/usr/bin/env python3
from sys import stdin


def find_index_of_first_four_non_repeating(input: str, distinct_characters: int = 4):
    for i in range(len(input) - distinct_characters):
        if len(set(input[i:i+distinct_characters])) == distinct_characters:
            return i + distinct_characters


def solve() -> None:
    input = stdin.readlines()
    print(list(map(find_index_of_first_four_non_repeating, input)))
    print(list(map(lambda x: find_index_of_first_four_non_repeating(x, 14), input)))


if __name__ == '__main__':
    solve()
