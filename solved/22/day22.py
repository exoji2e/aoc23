#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 22
def get_year(): return 2023

def parse(ln):
    l, r = ln.split('~')
    L, R = lazy_ints(l.split(',')), lazy_ints(r.split(','))
    return min(L, R), max(L, R)

def getCoords(brick):
    L, R = brick
    if L == R:
        return [tuple(L)]
    for cId in range(3):
        if L[cId] != R[cId]:
            mn, mx = min(L[cId], R[cId]), max(L[cId], R[cId])
            out = []
            for i in range(mn, mx+1):
                V = list(L)
                V[cId] = i
                out.append(tuple(V))
            return out

def getBelow(b):
    below = []
    for coord in getCoords(b):
        c2 = list(coord)
        c2[2] -= 1
        below.append(tuple(c2))
    return below
def getAbove(b):
    below = []
    for coord in getCoords(b):
        c2 = list(coord)
        c2[2] += 1
        below.append(tuple(c2))
    return below

def down(b):
    L, R = map(list, b)
    L[2] -= 1
    R[2] -= 1
    return tuple(L), tuple(R)

def fall(bricks):
    occ = {}
    newBricks = []
    for b, i in bricks:
        L, R = b

        while True:
            if b[0][2] == 1: break
            if any(c in occ for c in getBelow(b)):
                break
            b = down(b)
        for c in getCoords(b):
            occ[c] = i
        newBricks.append((b, i))
    return newBricks, occ

def getBricks(v):
    lns = get_lines(v)
    bricks = []
    for i, ln in enumerate(lns):
        bricks.append((parse(ln), i))
    bricks.sort(key=lambda x: x[0][0][2])
    return bricks

# not 440
def p1(v):
    bricks = getBricks(v)
    finalBricks, occ = fall(bricks)
    cantMove = set()
    for b, i in finalBricks:
        seen = set()
        for c in getBelow(b):
            if c in occ and occ[c] != i:
                seen.add(occ[c])
        if len(seen) == 1:
            cantMove.add(seen.pop())

    return len(bricks) - len(cantMove)

def p2(v):
    bricks = getBricks(v)
    finalBricks, occ = fall(bricks)
    graph = {i: set() for i in range(len(bricks))}
    for b, i in finalBricks:
        seen = set()
        for c in getBelow(b):
            if c in occ and occ[c] != i:
                seen.add(occ[c])
        for x in seen:
            graph[i].add(x)

    depends = {i: [] for i in range(len(bricks))}
    for k, v in graph.items():
        for ch in v:
            depends[ch].append(k)

    ans = 0
    for k, v in depends.items():
        rm = set([k])
        q = list(v)
        for u in q:
            if len(graph[u] & rm) == len(graph[u]):
                rm.add(u)
                for k in depends[u]:
                    q.append(k)
        ans += len(rm) - 1
    return ans


if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
