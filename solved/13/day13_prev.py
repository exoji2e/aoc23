#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 13
def get_year(): return 2023

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

def sameCol(G, c1, c2):
    return [ln[c1] for ln in G] == [ln[c2] for ln in G]

def matchesCol(G, col):
    N = len(G[0])
    for i in range(1, len(G[0])):
        c0 = col - i + 1
        c1 = col + i
        if not (c0 >= 0 and c1 < N): break
        if not sameCol(G, c0, c1):
            return False, 0
    return True, col + 1
def matchesRow(G, row):
    N = len(G)
    for i in range(1, len(G)):
        r0 = row - i + 1
        r1 = row + i
        if not (r0 >= 0 and r1 < N): break
        if G[r0] != G[r1]:
            return False, 0
    return True, row + 1

def findReflection(G, skip=(0, 0)):
    R, C = len(G), len(G[0])
    for r in range(0, R-1):
        ok, x = matchesRow(G, r)
        if ok and (100, x) != skip:
            return 100, x
    for c in range(0, C-1):
        ok, x = matchesCol(G, c)
        if ok and (1, x) != skip:
            return 1, x
    return None

def p1(v):
    chunks = v.split('\n\n')
    ans = 0
    for i, chunk in enumerate(chunks):
        G = [list(ln) for ln in chunk.split('\n')]
        ref = findReflection(G)
        ans += ref[0]*ref[1]

    return ans

def p2(v):
    chunks = v.split('\n\n')
    ans = 0
    for i, chunk in enumerate(chunks):
        done = False
        G = [list(ln) for ln in chunk.split('\n')]
        ref = findReflection(G)
        R, C = len(G), len(G[0])
        done = False
        for r in range(R):
            if done: break
            for c in range(C):
                old = G[r][c]
                G[r][c] = '#' if old == '.' else '.'
                ref2 = findReflection(G, skip=ref)
                G[r][c] = old
                if ref2 != None and ref2 != ref:
                    ans += ref2[0]*ref2[1]
                    done = True
                    break
        if not done:
            print(i)
            print(chunk)
        assert done

    return ans

if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
