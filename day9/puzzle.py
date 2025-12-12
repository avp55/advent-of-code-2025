from functools import lru_cache
import os
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush, heappushpop
import sys
from math import floor, ceil, sqrt, inf

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
    coords = []
    for line in input:
        y, x = [int(x) for x in line.split(",")]
        coords.append((x, y))
    mx = 0
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            p1 = coords[i]
            p2 = coords[j]
            xdiff = abs(p1[0] - p2[0]) + 1
            ydiff = abs(p1[1] - p2[1]) + 1
            mx = max(mx, xdiff * ydiff)
    print(mx)


def part2():
    input = read_input()


part1()
part2()
