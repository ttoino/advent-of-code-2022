import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

from parse import parse

with open("input") as inf, open("part1.out", "w+") as outf:
    sensors = [
        parse("Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}",
              i) for i in inf.read().splitlines()
    ]

    impossible = set()
    beacons = set()

    for x, y, bx, by in sensors:
        dist = abs(x - bx) + abs(y - by)

        ydist = abs(2000000 - y)
        xdist = dist - ydist

        impossible.update(range(x - xdist, x + xdist + 1))
        if by == 2000000:
            beacons.add(bx)

    outf.write(str(len(impossible - beacons)))
