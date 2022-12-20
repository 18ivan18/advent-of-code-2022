#!/usr/bin/env python3


from typing import List, Optional


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = self
        self.prev = self

    def print(self):
        n = self
        while True:
            print(n.value, end=' ')
            n = n.next
            if n == self:
                break
        print()

    def find(self, value: Optional[int] = None, index: Optional[int] = None):
        n, step = self, 0
        while True:
            if value == n.value:
                return n
            if index == step:
                return n
            n = n.next
            step += 1
            if n == self:
                break
        return n

    def move(self, l):
        if self.value == 0:
            return

        # order the prev and next nodes
        self.prev.next = self.next
        self.next.prev = self.prev

        # find new prev
        prev, next, v = self.prev, self.next, self.value % (l-1)
        for _ in range(v):
            prev = prev.next if v > 0 else prev.prev
            next = next.next if v > 0 else next.prev

        prev.next = self
        self.prev = prev
        next.prev = self
        self.next = next


def solve(b: List[str], decryption_key: int = 1, mixing_rounds: int = 1):
    a = [Node(int(x)*decryption_key) for x in b]
    for prev, next in zip(a[:-1], a[1:]):
        prev.next = next
        next.prev = prev
    a[-1].next = a[0]
    a[0].prev = a[-1]
    zero = a[0].find(0)
    # zero.print()
    length = len(a)
    for _ in range(mixing_rounds):
        for n in a:
            n.move(length)
        # zero.print()
    return sum([zero.find(index=x % length).value for x in (1000, 2000, 3000)])


if __name__ == '__main__':
    a = [x for x in open(0).read().strip().splitlines()]
    print(solve(a))
    print(solve(a, decryption_key=811589153, mixing_rounds=10))
