import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    outf.write(
        str(
            next(
                iter(
                    filter(lambda x: len(set(x[1])) == 14,
                           enumerate(mit.windowed(inf.read(), 14)))))[0] + 14))
