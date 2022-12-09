import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

DIRS = {'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1)}


def sign(x: int):
    return x and x // abs(x)


with open("input") as inf, open("part2.out", "w+") as outf:
    pos = [(0, 0) for _ in range(10)]

    tail_poss = set()

    for i in inf.read().splitlines():
        dir, amount = i.split()
        amount = int(amount)

        for i in range(amount):
            for j, p in enumerate(pos):
                if j == 0:
                    d = DIRS[dir]
                    pos[j] = p[0] + d[0], p[1] + d[1]
                else:
                    d = pos[j - 1][0] - p[0], pos[j - 1][1] - p[1]

                    if abs(d[0]) > 1 or abs(d[1]) > 1:
                        pos[j] = p[0] + sign(d[0]), p[1] + sign(d[1])

            tail_poss.add(pos[-1])

    outf.write(str(len(tail_poss)))