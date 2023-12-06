#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 6
def get_year(): return 2023

def parse(ln):
    return lazy_ints(ln.split())[1:]
def parse2(ln):
    _, x = ln.split(':')
    return int(x.replace(' ', ''))

def count(T, D):
    c = 0
    for x in range(1, T):
        if x*(T-x) > D:
            c += 1
    return c

def p1(v):
    lns = get_lines(v)
    ans = 1
    T = parse(lns[0])
    D = parse(lns[1])
    for t, d in zip(T, D):
        ans *= count(t, d)
    return ans

def p2(v):
    lns = get_lines(v)
    T = parse2(lns[0])
    D = parse2(lns[1])
    return count(T, D)


if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
