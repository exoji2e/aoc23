#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
import numpy as np
def get_day(): return 21
def get_year(): return 2023

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

def walk(S, G, cnt):
    R, C = len(G), len(G[0])
    dist = {S:0}
    q = [S]
    for i in range(1,cnt+1):
        q2 = []
        for x, y in q:
            for nx, ny in grid4n(x, y):
                if G[nx%R][ny%C] == '#': continue
                if (nx, ny) not in dist:
                    q2.append((nx, ny))
                    dist[nx, ny] = i
        q = q2
    return dist
DP = {}

def count(S, G, steps):
    dist = walk(S, G, steps)
    return len([1 for k, v in dist.items() if v%2 == steps%2])

def p1(v):
    G = get_lines(v)
    S = None
    for i, row in enumerate(G):
        for j, ch in enumerate(row):
            if ch == 'S':
                S = i, j
    return count(S, G, 64)

def p2(v):
    G = get_lines(v)
    S = None
    for i, row in enumerate(G):
        for j, ch in enumerate(row):
            if ch == 'S':
                S = i, j
    Y = []
    X = [0, 1, 2]
    for i in X:
        Y.append(count(S, G, 131*i + 65))

    a, b, c = map(round, np.polyfit(X, Y, 2))

    n = (26501365 - 65)//131
    return round(a*n*n + b*n + c)


if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
