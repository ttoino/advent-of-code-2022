import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

DIRS = {'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1)}


def sign(x: int):
    return x and x // abs(x)


with open("input") as inf, open("part1.out", "w+") as outf:
    tail_pos = (0, 0)
    head_pos = (0, 0)

    tail_poss = set()

    for i in inf.read().splitlines():
        dir, amount = i.split()
        amount = int(amount)

        for i in range(amount):
            d = DIRS[dir]
            head_pos = head_pos[0] + d[0], head_pos[1] + d[1]

            tail_d = head_pos[0] - tail_pos[0], head_pos[1] - tail_pos[1]

            if abs(tail_d[0]) > 1 or abs(tail_d[1]) > 1:
                tail_pos = tail_pos[0] + sign(tail_d[0]), tail_pos[1] + sign(
                    tail_d[1])

            tail_poss.add(tail_pos)

    outf.write(str(len(tail_poss)))