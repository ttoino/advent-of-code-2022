import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    cratesInp, instructions = inf.read().split("\n\n")
    cratesInp = reversed(cratesInp.splitlines()[:-1])

    crates = [list() for _ in range(9)]

    for l in cratesInp:
        for i, c in enumerate(crates):
            crate = l[i * 4 + 1]
            if crate != ' ':
                c.append(crate)

    for i in instructions.splitlines():
        _, count, _, start, _, end = i.split()

        crates[int(end) - 1].extend(crates[int(start) - 1][-int(count):])
        for _ in range(int(count)):
            crates[int(start) - 1].pop()

    outf.write("".join(c[-1] for c in crates))
