import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    outf.write(
        str(
            sum(
                int((a[0] >= a[2] and a[1] <= a[3]) or
                    (a[0] <= a[2] and a[1] >= a[3]))
                for a in (tuple(map(int, re.split(r'[,-]', i)))
                          for i in inf.read().splitlines()))))
