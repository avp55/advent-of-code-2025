import os
from collections import defaultdict, Counter
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


def convert_line_to_nums(line):
    return [int(x) for x in line.split()]


def read_input_converted(input):
    return [convert_line_to_nums(line) for line in input]


def is_paper(i, j, grid):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return 0
    return 1 if grid[i][j] == "@" else 0


def paper_removal(grid, should_remove=False):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != "@":
                continue
            opts = [
                (i - 1, j),
                (i + 1, j),
                (i, j - 1),
                (i, j + 1),
                (i - 1, j + 1),
                (i - 1, j - 1),
                (i + 1, j - 1),
                (i + 1, j + 1),
            ]
            results = sum([is_paper(i, j, grid) for i, j in opts])
            if results < 4:
                total += 1
                if should_remove:
                    grid[i][j] = "."
    return total


def part1():
    input = read_input()
    grid = []
    for i in input:
        grid.append(i)
    total = paper_removal(grid)

    print(total)


def part2():
    input = read_input()
    grid = []
    for i in input:
        grid.append(list(i))
    total = 0
    while True:
        res = paper_removal(grid, True)
        if res == 0:
            break
        total += res
    print(total)


part1()
part2()
