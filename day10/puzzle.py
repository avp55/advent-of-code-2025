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


def bfs():
    pass


def next_queue_items(prev_board_state, prev_cost, index_options, queue, seen):
    for opt in index_options:
        new_board_state = prev_board_state[:]
        for num in opt:
            new_board_state[num] = "." if new_board_state[num] == "#" else "#"
        new_state_str = "".join(new_board_state)
        if new_state_str in seen:
            continue
        queue.append((prev_cost + 1, new_board_state))
        seen.add(new_state_str)


def part1():
    input = read_input()
    total = 0
    for line in input:

        line = line.split()
        req_state = None
        index_opts = []
        for item in line:
            if "[" in item:
                item = item[1 : len(item) - 1]
                req_state = item
            elif "{" in item:
                continue
            else:
                item = item[1 : len(item) - 1]
                index_presses = item.split(",")
                index_presses = [int(x) for x in index_presses]
                index_opts.append(index_presses)
        initial_state = ["."] * len(req_state)
        q = deque([])
        seen = set()
        next_queue_items(initial_state, 0, index_opts, q, seen)
        min_cost = inf
        while q:
            cost, item = q.popleft()
            if "".join(item) == req_state:
                min_cost = cost
                break
            next_queue_items(item, cost, index_opts, q, seen)
        total += min_cost
    print(total)


def part2():
    input = read_input()


part1()
part2()
