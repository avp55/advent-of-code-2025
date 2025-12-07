from functools import lru_cache
import os
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush, heappushpop
import sys
from math import floor, ceil

sys.setrecursionlimit(150000)


def read_input() -> "list[str]":
    input: list[str] = []
    here = os.path.dirname(os.path.abspath(__file__))

    filename = os.path.join(here, "input1.txt")
    with open(filename) as file:
        for line in file:
            input.append(line.strip())
    return input


def read_input_no_strip() -> "list[str]":
    input: list[str] = []
    here = os.path.dirname(os.path.abspath(__file__))

    filename = os.path.join(here, "input1.txt")
    with open(filename) as file:
        for line in file:
            input.append(line.strip("\n"))
    return input


def convert_line_to_nums(line):
    return [int(x) for x in line.split()]


def read_input_converted(input):
    return [convert_line_to_nums(line) for line in input]


def part1():
    input = read_input()
    grid = []
    for line in input:
        grid.append(line)
    sx, sy = None, None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                sx, sy = i, j
                break
    q = deque([(sx, sy)])
    visited = set()
    split = 0
    while q:
        x, y = q.popleft()
        if x + 1 >= len(grid):
            continue
        nx, ny = x + 1, y
        if grid[nx][ny] == "^":
            lx, ly = nx, ny - 1
            rx, ry = nx, ny + 1
            is_split = False
            if (lx, ly) not in visited and ly > -1:
                q.append((lx, ly))
                is_split = True
                visited.add((lx, ly))
            if (rx, ry) not in visited and ry < len(grid[0]):
                q.append((rx, ry))
                visited.add((rx, ry))
                is_split = True
            if is_split:
                split += 1
        else:
            if (nx, ny) not in visited:
                q.append((nx, ny))
                visited.add((nx, ny))
    print(split)


def part2():
    input = read_input()
    grid = []
    for line in input:
        grid.append(line)
    sx, sy = None, None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                sx, sy = i, j
                break

    @lru_cache
    def dfs(x, y):
        if x >= len(grid) or y >= len(grid[0]) or y < 0:
            return 0
        nx, ny = x + 1, y
        if nx >= len(grid):
            return 1
        if grid[nx][ny] != "^":
            return dfs(nx, ny)
        opt1 = dfs(nx, ny - 1)
        opt2 = dfs(nx, ny + 1)
        return opt1 + opt2

    print(dfs(sx, sy))


part1()
part2()
