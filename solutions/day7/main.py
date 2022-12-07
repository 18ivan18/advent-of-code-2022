#!/usr/bin/env python3

from functools import reduce
from sys import stdin
from typing import List, Optional,  Union


class File():
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def to_string(self, index: int):
        return " " * (index * 2) + f"- {self.name} (file, size={self.size})"

    def get_total_size(self):
        return self.size


class Directory():
    def __init__(self, name: str = '', parent=None):
        self.name = name
        self.files: List[Union[File, Directory]] = []
        self.parent = parent
        self.total_size: Optional[int] = None

    def add_file(self, file: File):
        self.files.append(file)

    def add_dir(self, dir):
        self.files.append(dir)
        dir.parent = self

    def get_child(self, name: str):
        for f in self.files:
            if f.name == name and isinstance(f, Directory):
                return f
        raise ValueError

    def get_total_size(self):
        if self.total_size is None:
            self.total_size = reduce(
                lambda curr, next: curr + next.get_total_size(), self.files, 0)
        return self.total_size

    def to_string(self, index: int = 0):
        ret = " " * (index * 2) + \
            f"- {self.name} (dir) - {self.get_total_size()}\n"
        for f in self.files:
            ret += f.to_string(index+1) + '\n'
        return ret

    def get_all_dirs_with_size_compared_to_threshold(self, threshold: int, comparator=lambda x, y: x < y) -> List[int]:
        result: List[int] = []
        if comparator(self.get_total_size(), threshold):
            result.append(self.get_total_size())
        for f in self.files:
            if isinstance(f, Directory):
                result += f.get_all_dirs_with_size_compared_to_threshold(
                    threshold, comparator)
        return result


def solve() -> None:
    root = Directory('/')
    input = stdin.read().splitlines()
    for line in input[1:]:
        if line == '$ ls':
            continue
        if line.startswith('$ cd '):
            dir_name = line.split('$ cd ')[1]
            if dir_name == '..':
                root = root.parent
                continue
            root = root.get_child(dir_name)
            continue
        if line.startswith('dir '):
            root.add_dir(Directory(line.split('dir ')[1]))
            continue
        size, name = line.split(' ')
        root.add_file(File(name, int(size)))

    while root is not None and root.parent is not None:
        root = root.parent

    print(root.to_string())
    print(sum(root.get_all_dirs_with_size_compared_to_threshold(100000)))
    update_size = 30000000
    max_size = 70000000
    space_needed = update_size - (max_size-root.get_total_size())
    print(min(root.get_all_dirs_with_size_compared_to_threshold(
        space_needed, lambda x, y: x > y)))


if __name__ == '__main__':
    solve()
