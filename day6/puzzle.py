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
    ops = []
    nums = []
    for line in input:
        line = line.split()
        if "+" in line or "*" in line:
            ops = line
        else:
            nums.append([int(x) for x in line])
    total = 0
    for j in range(len(nums[0])):
        op = ops[j]
        col_total = 1 if op == "*" else 0
        for i in range(len(nums)):
            c = nums[i][j]
            if op == "*":
                col_total *= c
            else:
                col_total += c
        total += col_total
    print(total)


def part2():
    input = read_input_no_strip()
    ops = []
    nums = []
    operators = ["+", "*"]
    for line in input:
        if any(op in line for op in operators):
            ops = line
        else:
            nums.append(line)
    total = 0
    to_do = []
    for j in range(len(nums[0])):
        op = ops[j]
        col_nums = []
        for i in range(len(nums)):
            col_nums.append(nums[i][j])
        potential_num = ("".join(col_nums)).strip()
        if potential_num == "":
            continue
        potential_num = int(potential_num)
        if to_do and (to_do[0] in operators) and (op in operators):
            btop = to_do.pop(0)
            bt = 0 if btop == "+" else 1
            while to_do:
                if btop == "+":
                    bt += to_do.pop()
                else:
                    bt *= to_do.pop()
            total += bt
            to_do = []
        if op in operators:
            to_do.append(op)
        to_do.append(potential_num)

    if to_do:
        btop = to_do.pop(0)
        bt = 0 if btop == "+" else 1
        while to_do:
            if btop == "+":
                bt += to_do.pop()
            else:
                bt *= to_do.pop()
        total += bt
    print(total)


part1()
part2()
