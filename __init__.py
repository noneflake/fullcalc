# coding: utf-8
# fullcalc by noneflake

from __future__ import annotations
from typing     import Union


def sl(s, i: int) -> str:
    return s[:i]

def sr(s, i: int) -> str:
    return s[i+1:]

""" Unused (updated before repo creation)
def findAny(s: str, *subs: tuple[str]) -> bool:
    for sub in subs:
        if s.find(sub) != -1:
            return True
    return False
"""

ops: list[tuple[str, callable]] = [
    ("+", (lambda a, b: a + b)),
    ("-", (lambda a, b: a - b)),
    ("*", (lambda a, b: a * b)),
    ("/", (lambda a, b: a / b)),
    ("^", (lambda a, b: a ** b))
]


def precalc(s: str) -> list[Union[float, str]]:
    lst : list[Union[float, str]] = []
    rops: str = "".join([e[0] for e in ops])
    tnum: str = None
    for i, c in enumerate(s):
        if c in "0123456789":
            if tnum is None:
                tnum = str()
            tnum += c
            if i == len(s)-1:
                lst.append(float(tnum))
                tnum = None
            continue

        if tnum is not None:
            lst.append(float(tnum))
            tnum = None

        if c in rops:
            lst.append(c)
    print(lst)
    return lst


def calc(s: list[Union[int, float, str]]) -> float:
    num: Union[float, int] = None
    for op, opr in ops:
        for i, t in enumerate(s):
            if t == op:
                return opr(calc(sl(s, i)), calc(sr(s, i)))
            if isinstance(t, (int, float)):
                num = t
    return num

# Usage : calc(precalc("0*4+6/2^2"))
