import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, deque

monkeys = []
divisor = 0


class Monkey:

    __slots__ = ('items', 'operation', 'test', 'true_monkey', 'false_monkey',
                 'inspections')

    def __init__(self, i: deque[int], op: str, d: int, t: int, f: int):
        self.items = i
        self.operation = op
        self.test = d
        self.true_monkey = t
        self.false_monkey = f
        self.inspections = 0

    @classmethod
    def parse(cls, s: str):
        s = s.splitlines()

        i = deque(int(i) for i in s[1].split(": ")[1].split(', '))
        op = s[2].split("= ")[1]
        d = int(s[3].split("by ")[1])
        t = int(s[4][-1])
        f = int(s[5][-1])

        return cls(i, op, d, t, f)

    def inspect(self):
        self.inspections += len(self.items)
        for _ in range(len(self.items)):
            old = self.items.popleft()
            i = eval(self.operation)
            i %= divisor

            if i % self.test == 0:
                monkeys[self.true_monkey].items.append(i)
            else:
                monkeys[self.false_monkey].items.append(i)


with open("input") as inf, open("part2.out", "w+") as outf:
    monkeys = list(map(Monkey.parse, inf.read().split("\n\n")))
    divisor = ft.reduce(op.mul, map(lambda x: x.test, monkeys), 1)

    for i in range(10000):
        print(i, end='\r')
        for m in monkeys:
            m.inspect()

    monkeys.sort(key=lambda x: x.inspections)
    outf.write(str(monkeys[-1].inspections * monkeys[-2].inspections))
