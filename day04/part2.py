import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    outf.write(
        str(
            sum(
                int(
                    len(
                        set(range(a[0], a[1] +
                                  1)).intersection(set(range(a[2], a[3] +
                                                             1)))) > 0)
                for a in (tuple(map(int, re.split(r'[,-]', i)))
                          for i in inf.read().splitlines()))))
