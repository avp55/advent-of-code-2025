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


def part1():
    input = read_input()
    start = 50
    total = 0
    for line in input:
        dir = 1 if line[0] == "R" else -1
        amount = int(line[1:]) * dir

        start += amount
        start %= 100
        if start == 0:
            total += 1
    print(total)
    return total


def part2():
    input = read_input()
    start = 50
    total = 0
    for line in input:
        dir = 1 if line[0] == "R" else -1
        amount = int(line[1:]) * dir

        end = start + amount
        low = min(start, end)
        high = max(start, end)

        count = (high // 100) - ((low - 1) // 100)

        if start % 100 == 0:
            count -= 1

        total += count

        start = end % 100

    print(total)


part1()
part2()
