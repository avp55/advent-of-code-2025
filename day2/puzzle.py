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
    input = "".join(read_input())
    input = input.split(",")
    total = 0
    for item in input:
        l, r = item.split("-")
        for i in range(int(l), int(r) + 1):
            si = str(i)
            if len(si) % 2 != 0:
                continue
            m = len(si) // 2
            if si[:m] == si[m:]:
                total += i
                print(i)
    print(total)


def first_repeating_pattern(s: str):
    n = len(s)

    for size in range(n // 2, 0, -1):
        if n % size != 0:
            continue
        repeat_count = n // size
        if repeat_count < 2:
            continue

        if s[:size] * repeat_count == s:
            return True
    return False


def seq(number: str):
    c = Counter(number)
    sum(c.values()) % 2 == 0
    if len(c.values()) == 1:
        return True
    if 1 in c.values():
        return False
    if len(number) % 2 != 0:
        vals = list(c.values())
        test = vals[0]
        for v in vals:
            if v != test:
                return False

    return first_repeating_pattern(number)


def part2():
    input = "".join(read_input())
    input = input.split(",")
    total = 0
    for item in input:
        l, r = item.split("-")
        for i in range(int(l), int(r) + 1):
            si = str(i)
            if seq(si):
                total += i

    print(total)


# part1()
part2()
