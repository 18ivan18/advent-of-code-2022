#!/usr/bin/env python3

from collections import deque
from copy import deepcopy
from sys import stdin
from typing import List


class Monkey():
    common_div = 1

    def __init__(self, monkey_str: str):
        monkey_str_lines = monkey_str.splitlines()
        self.id = int(monkey_str_lines[0][:-1].split('Monkey ')[1])
        self.items = deque([
            int(x) for x in monkey_str_lines[1].split('Starting items: ')[1].split(',')])
        self.operation = monkey_str_lines[2].split('Operation: new = ')[1]
        test_divisor = (
            int(monkey_str_lines[3].split('Test: divisible by ')[1]))
        Monkey.common_div *= test_divisor
        self.test = lambda x: x % test_divisor == 0
        self.throw_to_if_true = int(
            monkey_str_lines[4].split('If true: throw to monkey ')[1])
        self.throw_to_if_false = int(
            monkey_str_lines[5].split('If false: throw to monkey ')[1])
        self.monkeys: List[Monkey] = []
        self.inspected_items_count = 0
        self.worry = True

    def send_to(self, monkey_id: int, worry_level: int):
        self.monkeys[monkey_id].items.append(worry_level)

    def inspect_item(self, item_value: int):
        self.inspected_items_count += 1
        old = item_value
        worry_level = eval(self.operation)
        if self.worry:
            worry_level //= 3
        test = self.test(worry_level)
        worry_level %= Monkey.common_div
        self.send_to(
            self.throw_to_if_true if test else self.throw_to_if_false, worry_level)

    def inspect_items(self):
        while len(self.items):
            self.inspect_item(self.items[0])
            self.items.popleft()


def solve(monkeys: List[Monkey], worry: bool, rounds: int):
    monkeys = deepcopy(monkeys)
    for monkey in monkeys:
        monkey.monkeys = monkeys
        monkey.worry = worry

    for _ in range(rounds):
        for monkey in monkeys:
            monkey.inspect_items()

    for monkey in monkeys:
        print(
            f"Monkey {monkey.id} inspected items {monkey.inspected_items_count} times.")
    a, b = sorted(monkeys, key=lambda x: x.inspected_items_count,
                  reverse=True)[:2]
    return a.inspected_items_count*b.inspected_items_count


if __name__ == '__main__':
    monkeys = [Monkey(x) for x in stdin.read().split('\n\n')]
    print(solve(monkeys, worry=True, rounds=20))
    print(solve(monkeys, worry=False, rounds=10_000))
