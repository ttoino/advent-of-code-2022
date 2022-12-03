import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter


def turn(them, score):
    print(them, score, end=' ')

    them = ord(them) - ord('A') + 1
    score = ord(score) - ord('X')

    us = (score + them + 1) % 3 + 1

    print(them, us, score)

    return us + score * 3


with open("input") as inf, open("part2.out", "w+") as outf:
    outf.write(str(sum(turn(i[0], i[2]) for i in inf.readlines())))
