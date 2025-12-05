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


def merge_ranges(ranges):
    if not ranges:
        return []
    lo, hi = ranges[0][0], ranges[0][1]
    output = []
    for i in range(1, len(ranges)):
        cur_lo, cur_hi = ranges[i]
        if cur_lo > hi:
            output.append((lo, hi))
            lo = cur_lo
            hi = cur_hi
        else:
            hi = max(cur_hi, hi)
    output.append((lo, hi))
    return output


def target_in_ranges(merged, target):
    l, r = 0, len(merged) - 1
    while l <= r:
        mid = (l + r) // 2
        lo, hi = merged[mid]
        if target < lo:
            r = mid - 1
        elif target > hi:
            l = mid + 1
        else:
            return True
    return False


def part1():
    input = read_input()
    ranges = []
    ingredients = []
    for line in input:
        if not line:
            continue
        if "-" in line:
            low, hi = line.split("-")
            ranges.append((int(low), int(hi)))
        else:
            ingredients.append(int(line))
    ranges.sort()
    ranges = merge_ranges(ranges)
    fresh = []
    for i in ingredients:
        if target_in_ranges(ranges, i):
            fresh.append(i)
    print(len(fresh))


def part2():
    input = read_input()
    ranges = []
    for line in input:
        if not line:
            continue
        if "-" in line:
            low, hi = line.split("-")
            ranges.append((int(low), int(hi)))
    ranges.sort()
    ranges = merge_ranges(ranges)
    total = 0
    for lo, hi in ranges:
        total += hi - lo + 1
    print(total)


part1()
part2()
