import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

from icecream import ic

CYCLES = {20, 60, 100, 140, 180, 220}

with open("input") as inf, open("part1.out", "w+") as outf:
    x = 1
    cycle = 0
    vals = []

    def inc_cycle():
        global cycle
        cycle += 1

        ic(cycle, x)

        if cycle in CYCLES:
            vals.append(cycle * x)

    for i in inf.read().splitlines():
        if i.startswith("noop"):
            inc_cycle()
        elif i.startswith("addx"):
            inc_cycle()
            inc_cycle()
            x += int(i.split()[1])

    outf.write(str(sum(vals)))
