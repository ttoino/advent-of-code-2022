import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

lengths = []


def visit(node: dict[str, dict | int] | int):
    global lengths

    if isinstance(node, dict):
        s = 0

        for k, v in node.items():
            s += visit(v)

        lengths.append(s)

        return s

    return node


with open("input") as inf, open("part2.out", "w+") as outf:
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

    needed_space = visit(tree) - 40000000

    outf.write(str(min(filter(lambda x: x >= needed_space, lengths))))
