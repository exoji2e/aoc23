#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 8
def get_year(): return 2023

def parse(lines):
    G = {}
    for ln in lines:
        a, b, c = multi_split(ln, ' = (,)')
        G[a] = (b, c)
    return G


def p1(v):
    chunks = v.split('\n\n')
    ins = chunks[0]
    G = parse(chunks[1].split('\n'))
    node = 'AAA'
    s = 0
    while node != 'ZZZ':
        move = 0 if ins[s%len(ins)] == 'L' else 1
        node = G[node][move]
        s += 1
    return s

def loop_walk(node, G, ins):
    s = 0
    seen = {}
    walk = []
    L = len(ins)
    while (node, s%L) not in seen:
        seen[node, s%L] = s
        walk.append(node)
        move = 0 if ins[s%len(ins)] == 'L' else 1
        node = G[node][move]
        s += 1
    return walk, seen[node, s%len(ins)]

import math
def lcm(X):
    pw = X[0]
    for x in X[1:]:
        pw = (pw*x)//math.gcd(x, pw)
    return pw

def p2(v):
    chunks = v.split('\n\n')
    ins = chunks[0]
    G = parse(chunks[1].split('\n'))
    nodes = []
    for key in G.keys():
        if key[-1] == 'A':
            nodes.append(key)
    Xs = []
    for n in nodes:
        walk, loopBackPos = loop_walk(n, G, ins)
        a = [(node, i) for (i, node) in enumerate(walk) if node[-1] == 'Z']
        Lw = len(walk)
        mod = Lw - loopBackPos
        target = a[0][1] - loopBackPos + Lw
        Xs.append(((target)%mod, mod))
    # apparently all targets are 0 (no offsets from first z enounter and second. No need to do crt...
    mods = [mod for _, mod in Xs]
    return lcm(mods)


if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
