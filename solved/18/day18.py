#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 18
def get_year(): return 2023

def parseHex(hxf):
    S = hxf[2:-1]
    return int(S[-1]), int(S[:-1], 16)


def parse(ln):
    arr = ln.split()
    return arr[0], int(arr[1]), parseHex(arr[2])

DIRS = {
    0: (0, 1),
    1: (1, 0),
    2: (0, -1),
    3: (-1, 0),
    'R': (0, 1),
    'U': (1, 0),
    'L': (0, -1),
    'D': (-1, 0),
}

def area(polygon):
    A = 0
    for i in range(len(polygon)):
        x1, y1 = polygon[i-1]
        x2, y2 = polygon[i]
        A += (x1 + x2) * (y2 - y1)
    return abs(A/2)

def ptsCovered(polygon):
    import math
    def countBoundaryPoints(polygon):
        P = polygon
        cnt = 0
        for i in range(len(P)):
            dx = P[i][0] - P[i-1][0]
            dy = P[i][1] - P[i-1][1]
            cnt += math.gcd(abs(dx), abs(dy))
        return cnt
    A = area(polygon)
    p = countBoundaryPoints(polygon)
    cntInside = round(A - p/2 + 1)
    return cntInside + p

def p1(v):
    lns = get_lines(v)
    path = [(0, 0)]
    x, y = 0, 0
    for ln in lns:
        D, l, _ = parse(ln)
        dx, dy = DIRS[D]
        x, y = x + l*dx, y + l*dy
        path.append((x, y))
    return ptsCovered(path)

def p2(v):
    lns = get_lines(v)
    path = [(0, 0)]
    x, y = 0, 0
    for ln in lns:
        _, _, (D, l) = parse(ln)
        dx, dy = DIRS[D]
        x, y = x + l*dx, y + l*dy
        path.append((x, y))
    return ptsCovered(path)


if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
