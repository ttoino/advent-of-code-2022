import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

from time import sleep


def path(x1, y1, x2, y2):
    if x1 == x2:
        return map(lambda y: (x1, y), range(min(y1, y2), max(y1, y2) + 1))
    elif y1 == y2:
        return map(lambda x: (x, y1), range(min(x1, x2), max(x1, x2) + 1))


CLEAR_SCREEN = "\033[3J\033[H"

with open("input") as inf, open("part1.out", "w+") as outf:
    paths = [[tuple(map(int, j.split(',')))
              for j in i.split(" -> ")]
             for i in inf.read().splitlines()]

    rocks = set()
    sand = set()

    current_grain = (500, 0)

    for p in paths:
        for (x1, y1), (x2, y2) in it.pairwise(p):
            rocks.update(set(path(x1, y1, x2, y2)))

    min_x = min(map(op.itemgetter(0), rocks)) - 5
    max_x = max(map(op.itemgetter(0), rocks)) + 5

    min_y = 0
    max_y = max(map(op.itemgetter(1), rocks)) + 5

    while True:
        next_pos = (current_grain[0], current_grain[1] + 1)
        if next_pos in rocks | sand:
            next_pos = (next_pos[0] - 1, next_pos[1])
            if next_pos in rocks | sand:
                next_pos = (next_pos[0] + 2, next_pos[1])
                if next_pos in rocks | sand:
                    sand.add(current_grain)
                    next_pos = (500, 0)
        current_grain = next_pos

        if current_grain[1] > max_y:
            outf.write(str(len(sand)))
            exit()

        print(CLEAR_SCREEN, end='', flush=False)
        for y in range(current_grain[1] // 40 * 40,
                       current_grain[1] // 40 * 40 + 40):
            for x in range(min_x, max_x):
                print('█' if (x, y) in rocks else '░' if
                      (x, y) == current_grain else '▒' if
                      (x, y) in sand else ' ',
                      end='',
                      flush=False)

            print(flush=True)

        # sleep(0.01)
