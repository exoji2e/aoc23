#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 16
def get_year(): return 2023

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

mapL = {
    0: 3,
    1: 2,
    2: 1,
    3: 0
}
mapR = {
    0: 1,
    1: 0,
    2: 3,
    3: 2
}

def count(G, x, y, d):
    q = [(x, y, d)]
    vis = set(q)
    def step(x, y, d):
        dx, dy = DIRS[d]
        nx, ny = x + dx, y + dy
        T = nx, ny, d
        if 0 <= nx < len(G) and 0 <= ny < len(G[0]):
            if T not in vis:
                vis.add(T)
                q.append(T)
    for x, y, d in q:
        if G[x][y] == '.':
            step(x, y, d)
        elif G[x][y] == '/':
            d2 = mapL[d]
            step(x, y, d2)
        elif G[x][y] == '\\':
            d2 = mapR[d]
            step(x, y, d2)
        elif G[x][y] == '|':
            if d == 1 or d == 3:
                step(x, y, d)
            else:
                step(x, y, 1)
                step(x, y, 3)
        elif G[x][y] == '-':
            if d == 0 or d == 2:
                step(x, y, d)
            else:
                step(x, y, 0)
                step(x, y, 2)

    S = set({(x, y) for (x, y, _) in vis})

    return len(S)


def p1(v):
    lns = get_lines(v)
    G = [list(ln) for ln in lns]
    return count(G, 0, 0, 0)
def p2(v):
    lns = get_lines(v)
    G = [list(ln) for ln in lns]
    mx = 0
    for x in range(len(G)):
        mx = max(mx, count(G, x, 0, 0))
        mx = max(mx, count(G, x, len(G) - 1, 2))
    for y in range(len(G[0])):
        mx = max(mx, count(G, 0, y, 1))
        mx = max(mx, count(G, len(G[0]) - 1, y, 3))
    return mx


if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
