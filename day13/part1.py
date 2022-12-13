import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

import sys

sys.setrecursionlimit(100000)


def cmp(l1: list[list | int] | int, l2: list[list | int] | int):
    if type(l1) == type(l2) == int:
        return (l1 - l2) and (l1 - l2) // abs(l1 - l2)
    elif type(l1) == type(l2) == list:
        for i, j in zip(l1, l2):
            if cmp(i, j) == -1:
                return -1
            elif cmp(i, j) == 1:
                return 1
        return (len(l1) -
                len(l2)) and (len(l1) - len(l2)) // abs(len(l1) - len(l2))
    elif type(l1) == int:
        return cmp([l1], l2)
    else:
        return cmp(l1, [l2])


with open("input") as inf, open("part1.out", "w+") as outf:
    outf.write(
        str(
            sum(i + 1
                for i, (l1, l2) in enumerate(
                    i.splitlines() for i in inf.read().split("\n\n"))
                if cmp(eval(l1), eval(l2)) == -1)))
