#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 11
def get_year(): return 2023

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

def solve(v, extraCnt):
    lns = get_lines(v)
    ans = 0
    rows = set()
    cols = set()
    gxs = []
    for i, ln in enumerate(lns):
        for j, ch in enumerate(ln):
            if ch == '#':
                rows.add(i)
                cols.add(j)
                gxs.append((i, j))
    ans = 0
    def getDirCount(lo, hi, test):
        v = hi - lo
        for x in range(lo, hi):
            if x not in test:
                v += extraCnt
        return v
    for i in range(len(gxs)):
        x1, y1 = gxs[i]
        for j in range(i+1, len(gxs)):
            x2, y2 = gxs[j]
            ans += getDirCount(min(x1, x2), max(x1, x2), rows)
            ans += getDirCount(min(y1, y2), max(y1, y2), cols)

    return ans


def p1(v):
    return solve(v, 1)
def p2(v):
    return solve(v, 10**6 - 1)


if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
