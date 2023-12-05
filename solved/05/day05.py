#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 5
def get_year(): return 2023

def p1(v):
    chunks = v.split('\n\n')
    seeds = lazy_ints(chunks[0].split()[1:])

    MAPS = []
    for chunk in chunks[1:]:
        lines = chunk.split('\n')
        M = []
        for line in lines[1:]:
            M.append(lazy_ints(line.split()))
        M.sort(key=lambda x: x[1])
        MAPS.append(M)

    things = seeds
    def lookup(i, M):
        for d, s, l in M:
            e = s + l
            if s <= i < e:
                return d - s + i
        return i
    for M in MAPS:
        ths = []
        for t in things:
            ths.append(lookup(t, M))
        things = ths

    return min(things)

def p2(v):
    chunks = v.split('\n\n')
    sr = lazy_ints(chunks[0].split()[1:])
    seeds = []
    for i in range(0, len(sr), 2):
        seeds.append((sr[i], sr[i+1]))

    MAPS = []
    for chunk in chunks[1:]:
        lines = chunk.split('\n')
        M = []
        for line in lines[1:]:
            M.append(lazy_ints(line.split()))
        M.sort(key=lambda x: x[1])
        MAPS.append(M)

    things = seeds
    def lookup(T, M):
        S, L = T
        E = S + L
        last = S
        out = []
        for d, s, l in M:
            e = s + l
            if s <= S < e or s < E <= e:
                start = max(s, S)
                end = min(E, e)
                delta = d - s
                out.append((delta + start, end - start))
                if start > last:
                    out.append((last, start - last))
                last = end
        if last < E:
            out.append((last, E - last))
        return out
    for M in MAPS:
        ths = []
        for t in things:
            ths.extend(lookup(t, M))
        things = ths

    return min([t for t, _ in things])


if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
