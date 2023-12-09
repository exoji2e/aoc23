#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 9
def get_year(): return 2023

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

def diffs(arr):
    return [b - a for a, b in zip(arr, arr[1:])]

def finished(diffs):
    return all(i == 0 for i in diffs)

def p1(v):
    lns = get_lines(v)
    ans = 0
    for ln in lns:
        nbrs = parse(ln)
        tower = [nbrs]
        while not finished(nbrs):
            nbrs = diffs(nbrs)
            tower.append(nbrs)
        v = 0
        tower.pop()
        while tower:
            arr = tower.pop()
            v = arr[-1] + v

        ans += v
    return ans

def p2(v):
    lns = get_lines(v)
    ans = 0
    for ln in lns:
        nbrs = parse(ln)
        tower = [nbrs]
        while not finished(nbrs):
            nbrs = diffs(nbrs)
            tower.append(nbrs)
        v = 0
        tower.pop()
        while tower:
            arr = tower.pop()
            v = arr[0] - v

        ans += v
    return ans


if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
