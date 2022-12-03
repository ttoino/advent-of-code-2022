import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter


# turn(1, 1) => 3
# turn(1, 2) => 6
# turn(1, 3) => 0
# turn(2, 1) => 0
# turn(2, 2) => 3
# turn(2, 3) => 6
# turn(3, 1) => 6
# turn(3, 2) => 0
# turn(3, 3) => 3
def turn(them, us):
    print(them, us, end=' ')

    them = ord(them) - ord('A') + 1
    us = ord(us) - ord('X') + 1

    score = (us - them + 1) % 3 * 3

    print(them, us, score)

    return us + score


with open("input") as inf, open("part1.out", "w+") as outf:
    outf.write(str(sum(turn(i[0], i[2]) for i in inf.readlines())))
