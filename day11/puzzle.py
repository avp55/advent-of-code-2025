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
    mp = defaultdict(list)
    for line in input:
        fr_node, to_nodes = line.split(":")
        to_nodes = to_nodes.split()
        for node in to_nodes:
            mp[fr_node].append(node)

    @lru_cache(maxsize=None)
    def dfs(node):
        if node == "out":
            return 1
        total = 0
        for next_node in mp[node]:
            total += dfs(next_node)
        return total

    print(dfs("you"))


def part2():
    input = read_input()
    mp = defaultdict(list)
    for line in input:
        fr_node, to_nodes = line.split(":")
        to_nodes = to_nodes.split()
        for node in to_nodes:
            mp[fr_node].append(node)

    @lru_cache(maxsize=None)
    def dfs(node, is_dac, is_fft):
        if node == "out":
            return 1 if (is_dac and is_fft) else 0
        total = 0
        for next_node in mp[node]:
            total += dfs(
                next_node, is_dac or next_node == "dac", is_fft or next_node == "fft"
            )
        return total

    print(dfs("svr", False, False))


part1()
part2()
