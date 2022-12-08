import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter


def score(trees: list[list[int]], col: int, row: int, width: int, height: int):
    val = trees[row][col]

    up = 0
    for y in range(row - 1, -1, -1):
        up += 1
        if trees[y][col] >= val:
            break

    left = 0
    for x in range(col - 1, -1, -1):
        left += 1
        if trees[row][x] >= val:
            break

    down = 0
    for y in range(row + 1, height):
        down += 1
        if trees[y][col] >= val:
            break

    right = 0
    for x in range(col + 1, width):
        right += 1
        if trees[row][x] >= val:
            break

    return up * left * down * right


with open("input") as inf, open("part2.out", "w+") as outf:
    trees = [[int(i) for i in l] for l in inf.read().splitlines()]
    height = len(trees)
    width = len(trees[0])

    s = lambda x, y: score(trees, x, y, width, height)

    outf.write(str(max(s(x, y) for x in range(width) for y in range(height))))
