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


def dist3d(p1, p2):
    return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False

        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

        return True


def part1():
    input = read_input()
    coords = []
    for i, line in enumerate(input):
        x, y, z = [int(x) for x in line.split(",")]
        coords.append((x, y, z))
    num_edges = len(input)
    uf = UnionFind(num_edges)
    pairs = []
    for i in range(num_edges):
        for j in range(i + 1, num_edges):
            res = dist3d(coords[i], coords[j])
            pairs.append((res, i, j))
    heapify(pairs)
    i = 1000
    for i in range(1000):
        if not pairs:
            break
        _, fr, to = heappop(pairs)
        uf.union(fr, to)
    circuit_sizes = defaultdict(int)
    for i in range(num_edges):
        root = uf.find(i)
        circuit_sizes[root] += 1
    sizes = sorted(circuit_sizes.values(), reverse=True)
    result = sizes[0] * sizes[1] * sizes[2]
    print(result)


def part2():
    input = read_input()
    coords = []
    for i, line in enumerate(input):
        x, y, z = [int(x) for x in line.split(",")]
        coords.append((x, y, z))
    num_edges = len(input)
    uf = UnionFind(num_edges)
    pairs = []
    for i in range(num_edges):
        for j in range(i + 1, num_edges):
            res = dist3d(coords[i], coords[j])
            pairs.append((res, i, j))
    heapify(pairs)

    conns = None
    successful_merges = 0
    while successful_merges < num_edges - 1 and pairs:
        _, fr, to = heappop(pairs)
        if uf.union(fr, to):
            successful_merges += 1
            conns = (fr, to)
    fr_i = conns[0]
    to_i = conns[1]
    x1 = coords[fr_i][0]
    x2 = coords[to_i][0]
    print(x1 * x2)


part1()
part2()
