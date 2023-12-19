#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 19
def get_year(): return 2023

def parse(ln):
    key, rule = ln.split('{')
    rule = rule.replace('}', '')
    rules = rule.split(',')
    rls = []
    for rl in rules:
        if '<' in rl:
            o, v, x = multi_split(rl, '<:')
            v = int(v)
            rls.append(('<', o, v, x))
        elif '>' in rl:
            o, v, x = multi_split(rl, '>:')
            v = int(v)
            rls.append(('>', o, v, x))
        else:
            rls.append(('=', 0, 0, rl))

    return key, rls

def nxt(D, rule):
    for op, o, v, x in rule:
        if '<' == op:
            if D[o] < v:
                return x
        elif '>' == op:
            if D[o] > v:
                return x
        else:
            return x

def walk(D, rules):
    curr = 'in'
    while curr != 'A' and curr != 'R':
        curr = nxt(D, rules[curr])
    return curr

def valid(D):
    for lo, hi in D.values():
        if lo > hi:
            return False
    return True

def nxt2(D, rule):
    out = []
    for op, o, v, x in rule:
        if '<' == op:
            lo, hi = D[o]
            if lo < v:
                d0 = dict(D)
                d0[o] = (lo, min(v-1, hi))
                out.append((x, d0))
                D[o] = (v, hi)
        elif '>' == op:
            lo, hi = D[o]
            if hi > v:
                d0 = dict(D)
                d0[o] = (max(lo, v+1), hi)
                out.append((x, d0))
                D[o] = (lo, v)
        else:
            out.append((x, D))
        if not valid(D):
            return out
    return out

def size(D):
    prod = 1
    for a, b in D.values():
        prod *= b - a + 1
    return prod

def walk2(rules):
    curr = 'in'
    q = [('in', {k: (1, 4000) for k in 'xmas'})]
    ans = 0
    for curr, D in q:
        if curr == 'R': continue
        if curr == 'A':
            ans += size(D)
            continue
        for key, D2 in nxt2(D, rules[curr]):
            q.append((key, D2))
    return ans


def parseState(ln):
    ln = ln.replace('x', '"x"')
    ln = ln.replace('m', '"m"')
    ln = ln.replace('s', '"s"')
    ln = ln.replace('a', '"a"')
    ln = ln.replace('=', ':')
    D = eval(ln)
    return D

def p1(v):
    lns = get_lines(v)
    chunks = v.split('\n\n')
    lns = chunks[0].split('\n')
    rules = {}
    for key, rule in [parse(ln) for ln in lns]:
        rules[key] = rule
    ans = 0
    for ln in chunks[1].split('\n'):
        D = parseState(ln)
        x = walk(D, rules)
        if x == 'A':
            ans += sum(D.values())
    return ans

def p2(v):
    lns = get_lines(v)
    chunks = v.split('\n\n')
    lns = chunks[0].split('\n')
    rules = {}
    for key, rule in [parse(ln) for ln in lns]:
        rules[key] = rule

    return walk2(rules)


if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
