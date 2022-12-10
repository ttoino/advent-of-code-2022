import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

from icecream import ic

with open("input") as inf, open("part2.out", "w+") as outf:
    x = 1
    cycle = 0

    def inc_cycle():
        global x, cycle

        pos = cycle % 40

        print('█' if x - 1 <= pos <= x + 1 else ' ', end='')

        if pos == 39:
            print()

        cycle += 1

    for i in inf.read().splitlines():
        if i.startswith("noop"):
            inc_cycle()
        elif i.startswith("addx"):
            inc_cycle()
            inc_cycle()
            x += int(i.split()[1])

    outf.write(input("What do you see? "))
