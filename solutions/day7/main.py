#!/usr/bin/env python3

from functools import reduce
from sys import stdin
from typing import List, Optional,  Union


class File():
    def __init__(self, name: str, size: Optional[int] = None):
        self._name = name
        self._size = size

    def to_string(self, index: int):
        return " " * (index * 2) + f"- {self._name} (file, size={self._size})"

    @property
    def size(self):
        return self._size

    @property
    def name(self):
        return self._name


class Directory(File):
    def __init__(self, name: str = ''):
        super().__init__(name)
        self.files: List[File] = []

    def add(self, file: File):
        self.files.append(file)

    def get_subdir(self, name: str):
        for f in self.files:
            if f.name == name and isinstance(f, Directory):
                return f
        raise ValueError

    @property
    def size(self):
        if self._size is None:
            self._size = reduce(
                lambda curr, next: curr + next.size, self.files, 0)
        return self._size

    def to_string(self, index: int = 0):
        ret = " " * (index * 2) + \
            f"- {self._name} (dir)\n"
        for f in self.files:
            ret += f.to_string(index+1) + '\n'
        return ret

    def get_all_dirs_with_size_compared_to_threshold(self, threshold: int, comparator=lambda x, y: x < y):
        result: List[int] = []
        if comparator(self.size, threshold):
            result.append(self.size)
        for f in self.files:
            if isinstance(f, Directory):
                result += f.get_all_dirs_with_size_compared_to_threshold(
                    threshold, comparator)
        return result


def solve() -> None:
    dir_hierarchy = [Directory('/')]
    input = stdin.read().splitlines()
    for line in input[1:]:
        node = dir_hierarchy[-1]
        if line == '$ ls':
            continue
        if line.startswith('$ cd '):
            dir_name = line.split('$ cd ')[1]
            if dir_name == '..':
                dir_hierarchy.pop()
                continue
            dir_hierarchy.append(node.get_subdir(dir_name))
            continue
        if line.startswith('dir '):
            node.add(Directory(line.split('dir ')[1]))
            continue
        size, name = line.split(' ')
        node.add(File(name, int(size)))

    root = dir_hierarchy[0]
    print(root.to_string())
    print(sum(root.get_all_dirs_with_size_compared_to_threshold(100000)))

    update_size = 30000000
    max_size = 70000000
    space_needed = update_size - (max_size-root.size)
    print(min(root.get_all_dirs_with_size_compared_to_threshold(
        space_needed, lambda x, y: x > y)))


if __name__ == '__main__':
    solve()
