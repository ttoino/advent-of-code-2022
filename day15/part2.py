import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

from parse import parse

SIZE = 4000000


def dist(x, y, bx, by):
    return abs(x - bx) + abs(y - by)


with open("input") as inf, open("part2.out", "w+") as outf:
    sensors = [(x, y, dist(x, y, bx, by)) for x, y, bx, by in [
        parse("Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}",
              i) for i in inf.read().splitlines()
    ]]

    points = []

    for x, y, d in sensors:
        for px in range(x - d - 1, x + d + 2):
            if not (0 <= px <= SIZE):
                continue

            dd = abs(x - px)
            py1 = y + d + 1 - dd
            py2 = y - (d + 1 - dd)
            if 0 <= py1 <= SIZE:
                points.append((px, py1))
            if 0 <= py2 <= SIZE:
                points.append((px, py2))

        for x, y, d in sensors:
            points = list(filter(lambda p: dist(x, y, p[0], p[1]) > d, points))

        if len(points) > 0:
            break

    x, y = points[0]
    outf.write(str(x * 4000000 + y))
