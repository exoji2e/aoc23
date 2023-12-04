#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 4
def get_year(): return 2023

def p1(v):
    lns = get_lines(v)
    ans = 0
    for i, ln in enumerate(lns):
        ln = ln.split(':')[1]
        A, B = ln.split('|')
        W = set(lazy_ints(A.split()))
        Y = set(lazy_ints(B.split()))
        cnt = len([1 for y in Y if y in W])
        if cnt > 0:
            ans += 2**(cnt - 1)
    return ans

def p2(v):
    lns = get_lines(v)
    no = [1]*len(lns)
    for i, ln in enumerate(lns):
        ln = ln.split(':')[1]
        A, B = ln.split('|')
        W = set(lazy_ints(A.split()))
        Y = set(lazy_ints(B.split()))
        cnt = len([1 for y in Y if y in W])
        if cnt > 0:
            for j in range(i+1, i+1+cnt):
                if j < len(no):
                    no[j] += no[i]
    return sum(no)


if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
