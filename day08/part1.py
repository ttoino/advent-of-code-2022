import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    trees = [[int(i) for i in l] for l in inf.read().splitlines()]
    height = len(trees)
    width = len(trees[0])

    visible = set()

    for l in range(height):
        highest = -1
        for i in range(width):
            if trees[l][i] > highest:
                visible.add((i, l))
                highest = trees[l][i]

        highest = -1
        for i in range(width - 1, -1, -1):
            if trees[l][i] > highest:
                visible.add((i, l))
                highest = trees[l][i]

    for i in range(width):
        highest = -1
        for l in range(height):
            if trees[l][i] > highest:
                visible.add((i, l))
                highest = trees[l][i]

        highest = -1
        for l in range(height - 1, -1, -1):
            if trees[l][i] > highest:
                visible.add((i, l))
                highest = trees[l][i]

    outf.write(str(len(visible)))
