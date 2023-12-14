#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 14
def get_year(): return 2023

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

def roll(G):
    R, C = len(G), len(G[0])
    for c in range(C):
        curr = 0
        for r in range(R):
            if G[r][c] == 'O':
                if curr < r:
                    G[curr][c] = 'O'
                    G[r][c] = '.'
                curr += 1
            elif G[r][c] == '#':
                curr = r + 1

def spin(G):
    for i in range(4):
        roll(G)
        R, C = len(G), len(G[0])
        G = [[G[r][c] for r in range(R)[::-1]] for c in range(C)]
    return G

def toString(G):
    return '\n'.join(''.join(l) for l in G)

def load(G):
    R, C = len(G), len(G[0])
    ans = 0
    for c in range(C):
        curr = 0
        for r in range(R):
            if G[r][c] == 'O':
                ans += R - r
                curr += 1
            elif G[r][c] == '#':
                curr = r + 1
    return ans
def p1(v):
    G = [list(ln) for ln in get_lines(v)]
    roll(G)
    return load(G)

def p2(v):
    G = [list(ln) for ln in get_lines(v)]
    MAP = {}
    cnt = 0
    while True:
        cnt += 1
        G = spin(G)
        S = toString(G)
        if S in MAP:
            break
        MAP[S] = cnt
    target = 1000000000
    loopLen = cnt - MAP[S]
    steps = target - cnt
    loops = steps//loopLen
    steps -= loops*loopLen
    for _ in range(steps):
        G = spin(G)
    return load(G)


if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
