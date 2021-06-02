# coding: utf-8
# fullcalc by astergeist

from __future__ import annotations
from typing     import Union, Iterable, Callable


""" Unused (updated before repo creation)
def findAny(s: str, *subs: tuple[str]) -> bool:
    for sub in subs:
        if s.find(sub) != -1:
            return True
    return False
"""


ops: dict[str, Callable] = dict([
    ("+", (lambda a, b: a + b)),
    ("-", (lambda a, b: a - b)),
    ("*", (lambda a, b: a * b)),
    ("/", (lambda a, b: a / b)),
    ("^", (lambda a, b: a ** b))
])

oporder = [
    "+-",
    "*/",
    "^"
]

def precalc(s: str) -> list[Union[float, str]]:
    lst : list[Union[float, str]] = []
    rops: str = "".join([e[0] for e in ops.keys()])
    tnum: str = None
    for i, c in enumerate(s):
        if c in "0123456789.":
            if tnum is None:
                tnum = str()
            if c == "." and tnum.find(".") != -1:
                return None
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
    return [e for e in reversed(lst)]


def calc(lst: list[Union[float, str]]) -> float:
    num: float = None
    for oprd in oporder:
        for i, t in enumerate(lst):
            if isinstance(t, float):
                num = t
                continue
            if t in oprd:
                left  = lst[:i]
                right = lst[i+1:]
                rleft  = calc(left)
                rright = calc(right)
                rboth  = ops[t](rright, rleft)
                print(lst)
                print(f"<{right} : {rright}>  {t}  <{left} : {rleft}>  =  <{rboth}>")
                return rboth
    return num


test = ["0-77-2", "0.5*4^2-7"]
for e in test:
    print(f"Calc   > {calc(precalc(e))}\nPython > {eval(e.replace('^', '**'))}\n")
