#!/usr/bin/env python3

from copy import deepcopy
from sys import stdin


def get_number(monkeys, monkey_name) -> int:
    m, is_calculated, _ = monkeys[monkey_name]
    if is_calculated:
        return m
    first, sign, second = m.split(' ')
    result = eval(
        f"{get_number(monkeys, first)}{sign}{get_number(monkeys, second)}")
    monkeys[monkey_name] = [result, True, None]
    return int(result)


def part_1(monkeys):
    monkeys = deepcopy(monkeys)
    return get_number(monkeys, 'root')


def find_humn(monkeys, monkey_name):
    m, is_calculated, is_humn = monkeys[monkey_name]
    if is_calculated or is_humn:
        return is_humn
    first, sign, second = m.split(' ')
    is_first_humn = find_humn(monkeys, first)
    is_second_humn = find_humn(monkeys, second)
    if is_first_humn or is_second_humn:
        is_humn = True
    if not is_humn:
        result = int(eval(
            f"{monkeys[first][0]}{sign}{monkeys[second][0]}"))
        monkeys[monkey_name] = [result, True, is_humn]
    monkeys[monkey_name][2] = is_humn
    return is_humn

# second operand means if I'm looking for it or not


def calculate(sign, equality, other_value, second_operand=False):
    """
    a+b = x => b(a) = x-a(b)
    a-b = x => a = x+b, b=a-x
    a*b = x => a(b) = x/b(a)
    a/b = x => a = x*b, b = a/x
    """
    if sign == '+':
        return equality-other_value
    if sign == '-':
        if second_operand:
            return other_value-equality
        return other_value+equality
    if sign == '*':
        return int(equality/other_value)
    if sign == '/':
        if second_operand:
            return other_value/equality
        return other_value*equality


def get_humn_value(monkeys, start, equality):
    m, _, _ = monkeys[start]
    if start == 'humn':
        return equality
    first, sign, second = m.split(' ')
    fm, _, fh = monkeys[first]
    sm, _, sh = monkeys[second]
    if fh:
        return get_humn_value(monkeys, first, calculate(sign, equality, sm))
    if sh:
        return get_humn_value(monkeys, second, calculate(sign, equality, fm, second_operand=True))


def part_2(monkeys):
    monkeys = deepcopy(monkeys)
    monkeys['humn'] = ['HUMAN', False, True]
    m, _, _ = monkeys['root']
    first, _, second = m.split(' ')
    # print(first, second)
    is_first_humn = find_humn(monkeys, first)
    is_second_humn = find_humn(monkeys, second)
    equality = monkeys[second][0] if is_first_humn else first
    # print(f"{equality=}", monkeys)
    return get_humn_value(monkeys, first if is_first_humn else second, equality)


if __name__ == '__main__':
    monkeys = {}
    for line in stdin:
        name, operation = line.strip().split(': ')
        try:
            monkeys[name] = [int(operation), True, False]
        except:
            monkeys[name] = [operation, False, False]
    print(part_1(monkeys))
    print(part_2(monkeys))
