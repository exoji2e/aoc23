#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 17
def get_year(): return 2023

from heapq import heappop as pop, heappush as push
def dist(G):
    X, Y = len(G), len(G[0])
    INF = 10**18
    dist = defaultdict(lambda: INF)
    pq = []
    def add(i, dst):
        if dst < dist[i]:
            dist[i] = dst
            push(pq, (dst, i))
    add((0, 0, 0, 0), 0)
    add((0, 0, 1, 0), 0)
    def walk(x, y, d, cnt, c0):
        dx, dy = DIRS[d]
        nx, ny = x + dx, y + dy
        if 0 <= nx < X and 0 <= ny < Y:
            add((nx, ny, d, cnt), c0 + G[nx][ny])

    while pq:
        D, (x, y, d, cnt) = pop(pq)
        if (x, y) == (X-1, Y-1): return D
        if D != dist[(x, y, d, cnt)]: continue
        if cnt < 3:
            walk(x, y, d, cnt+1, D)
        dL = (d - 1)%4
        dR = (d + 1 )%4
        walk(x, y, dL, 1, D)
        walk(x, y, dR, 1, D)
def dist_p2(G):
    X, Y = len(G), len(G[0])
    INF = 10**18
    dist = defaultdict(lambda: INF)
    pq = []
    def add(i, dst):
        if dst < dist[i]:
            dist[i] = dst
            push(pq, (dst, i))
    add((0, 0, 0, 0), 0)
    add((0, 0, 1, 0), 0)
    def walk(x, y, d, cnt, c0):
        dx, dy = DIRS[d]
        nx, ny = x + dx, y + dy
        if 0 <= nx < X and 0 <= ny < Y:
            add((nx, ny, d, cnt), c0 + G[nx][ny])

    while pq:
        D, (x, y, d, cnt) = pop(pq)
        if (x, y) == (X-1, Y-1) and cnt >= 4: return D
        if D != dist[(x, y, d, cnt)]: continue
        if cnt < 10:
            walk(x, y, d, cnt+1, D)
        if cnt >= 4:
            dL = (d - 1)%4
            dR = (d + 1 )%4
            walk(x, y, dL, 1, D)
            walk(x, y, dR, 1, D)
def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def p1(v):
    lns = get_lines(v)
    G = [[int(ch) for ch in ln] for ln in lns]
    return dist(G)

def p2(v):
    lns = get_lines(v)
    G = [[int(ch) for ch in ln] for ln in lns]
    return dist_p2(G)


if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
