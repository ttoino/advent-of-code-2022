import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

import heapq as h

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def sum_tuples(*t):
    return ft.reduce(lambda x, y: tuple(i + j for i, j in zip(x, y)), t)


def dijkstra(start: tuple[int, int], end: tuple[int, int]):
    heap = [(0, *start)]
    visited = set()

    while len(heap):
        dist, x, y = h.heappop(heap)

        if (x, y) in visited:
            continue

        visited.add((x, y))
        val = ord(grid[y][x])

        if (x, y) == end:
            return dist

        for d in DIRS:
            new_x, new_y = sum_tuples((x, y), d)

            if new_x >= width or new_x < 0 or new_y >= height or new_y < 0:
                continue

            new_val = ord(grid[new_y][new_x])

            if new_val - val <= 1:
                h.heappush(heap, (dist + 1, new_x, new_y))

    return 100000000000000


with open("input") as inf, open("part2.out", "w+") as outf:
    grid = [list(l) for l in inf.read().splitlines()]

    start = []
    end = (0, 0)

    width = len(grid[0])
    height = len(grid)

    for y, l in enumerate(grid):
        for x, i in enumerate(l):
            if i == 'S' or i == 'a':
                start.append((x, y))
                grid[y][x] = 'a'
            elif i == 'E':
                end = (x, y)
                grid[y][x] = 'z'

    outf.write(str(min(dijkstra(p, end) for p in start)))
