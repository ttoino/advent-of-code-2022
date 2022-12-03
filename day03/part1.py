import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

from string import ascii_letters
from difflib import SequenceMatcher

with open("input") as inf, open("part1.out", "w+") as outf:
    outf.write(
        str(
            sum(
                ascii_letters.index(i[SequenceMatcher(
                    None, i[:len(i) // 2], i[len(i) //
                                             2:]).find_longest_match()[0]]) + 1
                for i in inf.readlines())))
