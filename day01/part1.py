import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    elves = [sum(map(int, e.splitlines())) for e in inf.read().split("\n\n")]

    outf.write(str(max(elves)))
