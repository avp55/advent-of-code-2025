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


def first_half_repeats(low, high):
    low_n = int(low)


def part1():
    input = read_input()
    total = 0
    for line in input:
        max_seen = float("-inf")
        max_pos = 0
        second_max = float("-inf")
        for i, c in enumerate([int(x) for x in line]):
            if i < len(line) - 1:
                if c > max_seen:
                    max_seen = c
                    max_pos = i
                    second_max = float("-inf")
            if c > second_max and i > max_pos:
                second_max = c
        total += (max_seen * 10) + second_max
    print(total)
    return 0


def part2_mono():
    input = read_input()
    total = 0
    for line in input:
        line = [int(x) for x in line]
        to_remove = len(line) - 12
        st = []
        for num in line:
            while st and st[-1] < num and to_remove > 0:
                st.pop()
                to_remove -= 1
            st.append(num)
        st = st[:12]
        st = [str(x) for x in st]
        total += int("".join(st))
    print(total)


def part2():
    input = read_input()
    total = 0
    for line in input:
        line = [int(x) for x in line]
        l_bound = 0
        r_bound = len(line) - 12 + 1
        res = 0
        for _ in range(12):
            max_seen = float("-inf")
            max_pos = 0
            for index in range(l_bound, r_bound):
                item = line[index]
                if item > max_seen:
                    max_seen = item
                    max_pos = index
            res *= 10
            res += max_seen
            r_bound += 1
            l_bound = max_pos + 1
        total += res
    print(total)


part1()
part2()
part2_mono()
