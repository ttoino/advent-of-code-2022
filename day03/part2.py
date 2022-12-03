import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

from string import ascii_letters

with open("input") as inf, open("part2.out", "w+") as outf:
    outf.write(
        str(
            sum(
                ascii_letters.index(next(iter(set.intersection(
                    *map(set, l))))) + 1
                for l in mit.chunked(inf.read().splitlines(), 3))))
