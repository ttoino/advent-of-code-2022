import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    outf.write(
        str(
            re.search(
                r"(?<=(.)(.)(.).)(?<!\1..)(?<!\1.)(?<!\1)(?<!\2.)(?<!\2)(?<!\3).",
                inf.read()).start()))
