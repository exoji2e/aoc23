#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 2
def get_year(): return 2023

def p1(v):
    lns = get_lines(v)
    ans = 0
    for i, ln in enumerate(lns):
        content = ln.split(':')[1]
        MX = Counter()
        for entry in multi_split(content, ',;'):
            no, c = lazy_ints(entry.strip().split())
            MX[c] = max(MX[c], no)
        if MX['red'] <= 12 and MX['green'] <= 13 and MX['blue'] <= 14:
            ans += i+1
    return ans

def p2(v):
    lns = get_lines(v)
    ans = 0
    for i, ln in enumerate(lns):
        content = ln.split(':')[1]
        MX = Counter()
        for entry in multi_split(content, ',;'):
            no, c = lazy_ints(entry.strip().split())
            MX[c] = max(MX[c], no)
            ans += MX['red']*MX['green']*MX['blue']
    return ans


if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
