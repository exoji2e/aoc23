#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 12
def get_year(): return 2023

def parse(ln):
    r, n = ln.split()
    return r, lazy_ints(n.split(','))

def match(row, nbrs):
    DP = {}
    L = len(row)
    N = len(nbrs)
    def notHs(i):
        if i < len(row):
            return row[i] != '#'
        return True
    def isOk(s, c):
        return s.count('.') == 0 and len(s) == c
    def cnt(i, j):
        if j == N:
            if row[i:].count('#') == 0: return 1
            else: return 0
        if (i, j) in DP: return DP[i, j]
        if i >= L: return 0

        ch = row[i]

        l = nbrs[j]

        if ch == '.':
            DP[i, j] = cnt(i+1, j)
        elif ch == '?':
            v = cnt(i+1, j)
            if isOk(row[i: i+l], l) and notHs(i+l):
                v += cnt(i+l+1, j+1)
            DP[i, j] = v
        elif ch == '#':
            v = 0
            if isOk(row[i: i+l], l) and notHs(i+l):
                v += cnt(i+l+1, j+1)
            DP[i, j] = v
        return DP[i, j]

    res = cnt(0, 0)
    return res

def p1(v):
    lns = get_lines(v)
    ans = 0
    for ln in lns:
        r, nbrs = parse(ln)
        x = match(r, nbrs)
        ans += x
    return ans

def p2(v):
    lns = get_lines(v)
    ans = 0
    for ln in lns:
        r, nbrs = parse(ln)
        r2 = '?'.join([r for _ in range(5)])
        n2 = nbrs * 5
        x = match(r2, n2)
        ans += x
    return ans


if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
