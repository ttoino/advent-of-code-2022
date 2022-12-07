import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

sum = 0


def visit(node: dict[str, dict | int] | int):
    global sum

    if isinstance(node, dict):
        s = 0

        for k, v in node.items():
            s += visit(v)

        if s <= 100000:
            sum += s

        return s

    return node


with open("input") as inf, open("part1.out", "w+") as outf:
    cmds = inf.read().split("$ ")[1:]

    tree = {}
    curr = {}
    stack = []

    for cmd in cmds:
        cmd, *rest = cmd.split()

        if cmd == "cd":
            arg = rest[0]

            if arg == "/":
                curr = tree
            elif arg == "..":
                curr = stack.pop()
            else:
                stack.append(curr)
                curr = curr[arg]

        if cmd == "ls":
            for size, name in mit.chunked(rest, 2):
                if size == "dir":
                    curr[name] = {}
                else:
                    curr[name] = int(size)

    visit(tree)

    outf.write(str(sum))
