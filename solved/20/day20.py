#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
import math
def get_day(): return 20
def get_year(): return 2023

def parse(ln):
    src, dst = ln.split(' -> ')
    if src[0] == '&':
        src = ('&', src[1:])
    elif src[0] == '%':
        src = ('%', src[1:])
    else:
        src = ('normal', src)
    dst = multi_split(dst, ' ,')
    return src, dst

def extract(lns):
    states = {}
    items = {}
    rxPar = None
    for ln in lns:
        src, dst = parse(ln)
        kind, id = src
        if 'rx' in dst:
            rxPar = id
        if kind == '&':
            states[id] = {}
        elif kind == '%':
            states[id] = 0
        else:
            states[id] = 0
        items[id] = src, dst
    for src, dst in items.values():
        for d in dst:
            if d not in items: continue
            if items[d][0][0] == '&':
                states[d][src[1]] = 0
    doublePars = {k: -1 for k in states[rxPar].keys()}
    return items, states, doublePars


def push(items, states, cnt, doublePars):
    low = 1
    hi = 0
    q = [('button', 'broadcaster', 0)]
    for parent, id, pulse in q:
        if id not in items: continue
        # part 2
        if parent in doublePars and pulse == 1:
            doublePars[parent] = cnt

        src, dst  = items[id]
        state = states[id]
        if src[0] == '%':
            if pulse == 1: continue
            newState = 1 - state
            newPulse = newState
            states[id] = newState
        elif src[0] == '&':
            state[parent] = pulse
            if all(v for v in state.values()):
                newPulse = 0
            else:
                newPulse = 1
        else:
            newPulse = pulse
        for d in dst:
            if newPulse: hi += 1
            else: low += 1
            q.append((id, d, newPulse))
    return low, hi


def p1(v):
    lns = get_lines(v)
    items, states, _ = extract(lns)
    L, H = 0, 0
    for _ in range(1000):
        l, h = push(items, states, 0, {})
        L, H = L+l, H+h
    return L*H

def p2(v):
    lns = get_lines(v)
    items, states, doublePars = extract(lns)
    L, H = 0, 0
    i = 0
    while True:
        i += 1
        push(items, states, i, doublePars)
        if min(doublePars.values()) != -1: break
    lst = list(doublePars.values())
    lcm = 1
    for x in lst:
        lcm = math.lcm(lcm, x)
    return lcm


if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
