#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from runner import main, get_commands
from utils import *
from collections import *
def get_day(): return 24
def get_year(): return 2023

def parse(ln):
    return lazy_ints(multi_split(ln, ' ,@'))

def pts2line(p, q):
    return (-q[1] + p[1],
          q[0] - p[0],
          p[0]*q[1] - p[1]*q[0])

def line(l1, l2):
    a1,b1,c1 = l1
    a2,b2,c2 = l2
    cp = a1*b2 - a2*b1
    if cp != 0:
        return True, float(b1*c2 - b2*c1)/cp, float(a2*c1 - a1*c2)/cp
    else:
        return False, -1, -1

def isFuture(item, x):
    x0, _, _, vx0, _, _ = item
    t = (x - x0)/vx0
    return t > 0

def collide(i1, i2):
    x0, y0, _, vx0, vy0, _ = i1
    x1, y1, _, vx1, vy1, _ = i2
    l0 = pts2line((x0, y0), (x0+vx0, y0+vy0))
    l1 = pts2line((x1, y1), (x1+vx1, y1+vy1))
    ok, x, y = line(l0, l1)
    if ok:
        if isFuture(i1, x) and isFuture(i2, x):
            return True, x, y
    return False, 0, 0


def testBox(c):
    return 200000000000000 <= c <= 400000000000000

import z3

def solve(items):
    s = z3.Solver()
    x0 = z3.Int('x0')
    vx0 = z3.Int('vx0')
    y0 = z3.Int('y0')
    vy0 = z3.Int('vy0')
    z0 = z3.Int('z0')
    vz0 = z3.Int('vz0')
    for i, (x, y, z, vx, vy, vz) in enumerate(items):
        ti = z3.Int(f't_{i}')
        s.add(x0 + vx0*ti == x + vx*ti)
        s.add(y0 + vy0*ti == y + vy*ti)
        s.add(z0 + vz0*ti == z + vz*ti)
    print('checking..')
    s.check()
    model = s.model()
    vs = [model.evaluate(var).as_long() for var in [x0, y0, z0]]
    return sum(vs)

def p1(v):
    lns = get_lines(v)
    ans = 0
    items = []
    for ln in lns:
        item = parse(ln)
        items.append(item)
    N = len(items)
    for i in range(N):
        for j in range(i+1, N):
            ok, x, y = collide(items[i], items[j])
            if ok and testBox(x) and testBox(y):
                ans += 1
    return ans

def p2(v):
    lns = get_lines(v)
    items = []
    for ln in lns:
        item = parse(ln)
        items.append(item)
    return solve(items)


if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
