import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

from time import sleep


def sum_tuples(*t):
    return ft.reduce(lambda x, y: tuple(i + j for i, j in zip(x, y)), t)


def path(x1, y1, x2, y2):
    if x1 == x2:
        return map(lambda y: (x1, y), range(min(y1, y2), max(y1, y2) + 1))
    elif y1 == y2:
        return map(lambda x: (x, y1), range(min(x1, x2), max(x1, x2) + 1))


CLEAR_SCREEN = "\033[3J\033[H"

with open("input") as inf, open("part2.out", "w+") as outf:
    paths = [[tuple(map(int, j.split(',')))
              for j in i.split(" -> ")]
             for i in inf.read().splitlines()]

    rocks = set()
    sand = set()

    for p in paths:
        for (x1, y1), (x2, y2) in it.pairwise(p):
            rocks.update(set(path(x1, y1, x2, y2)))

    min_x = min(map(op.itemgetter(0), rocks)) - 100
    max_x = max(map(op.itemgetter(0), rocks)) + 100

    min_y = 0
    max_y = max(map(op.itemgetter(1), rocks)) + 2

    for x in range(min_x - 500, max_x + 500):
        rocks.add((x, max_y))

    while True:
        current_pos = (500, 0)
        to_add = set()

        obstacles = sand | rocks

        while True:
            to_add.add(current_pos)

            if (next_pos := sum_tuples(current_pos, (0, 1))) not in obstacles:
                to_add.clear()
                current_pos = next_pos
            elif (next_pos := sum_tuples(current_pos,
                                         (-1, 1))) not in obstacles:
                if sum_tuples(current_pos, (1, 1)) not in obstacles:
                    to_add.clear()
                current_pos = next_pos
            elif (next_pos := sum_tuples(current_pos, (1, 1))) not in obstacles:
                current_pos = next_pos
            else:
                break

        sand.update(to_add)

        if (500, 0) in sand:
            outf.write(str(len(sand)))
            break

        print(CLEAR_SCREEN, end='', flush=False)
        for y in range(min_y, max_y):
            for x in range(min_x, max_x):
                print('█' if (x, y) in rocks else '▒' if
                      (x, y) in sand else ' ',
                      end='',
                      flush=False)

            print(flush=True)

        # sleep(0.01)
