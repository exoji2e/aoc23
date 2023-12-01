#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 1
def get_year(): return 2023

def p1(v):
    lns = get_lines(v)
    ans = 0
    for ln in lns:
        dgs = []
        for ch in ln:
            if '0' <= ch <= '9':
                dgs.append(int(ch))
        ans += dgs[0]*10 + dgs[-1]
    return ans

def p2(v):
    words = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    lns = get_lines(v)
    ans = 0
    for ln in lns:
        dgs = []
        for i in range(len(ln)):
            if '0' <= ln[i] <= '9':
                dgs.append(int(ln[i]))
            for k, nbr in words.items():
                if ln[i:i+len(k)] == k:
                    dgs.append(nbr)
        ans += dgs[0]*10 + dgs[-1]
    return ans
    return p1(v)


if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
