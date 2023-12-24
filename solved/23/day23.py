#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 23
def get_year(): return 2023

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to

    return wrappedfunc


def solve(adj, G):
    R, C = len(G), len(G[0])
    RES = {}
    for k, v in list(adj.items()):
        if len(v) == 1:
            no = 0
            oK = k
            pK = k
            path = []
            while len(v) == 1:
                pK = k
                k = v[0]
                path.append((k[0], k[1]))
                v = adj[k]
                no += 1
            RES[oK] = (k, (k[0], k[1]), no)


    best = [0]
    @bootstrap
    def longest(T, vis, d = 0):
        if T[0] == R - 1:
            if d > best[0]:
                #print('new best depth', d)
                best[0] = max(best[0], d)
            yield 0
            return
        if T in RES:
            k, el, no = RES[T]
            if el in vis:
                yield 0
                return
            vis.add(el)
            res = yield longest(k, vis, no + d)
            vis.remove(el)
            yield 0
        else:
            for T2 in adj[T]:
                if T2 not in vis:
                    cell = T2[0], T2[1]
                    vis.add(cell)
                    res = yield longest(T2, vis, d + 1)
                    vis.remove(cell)
            yield 0
    longest((0, 1, 0), set([(0, 1)]))
    return best[0]

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def testDir(dir, ch):
    if ch == '.': return True
    if ch == '#': return False
    if ch == '>': return dir == 0
    if ch == 'v': return dir == 1
    if ch == '<': return dir == 2
    if ch == '^': return dir == 3

def p1(v):
    G = get_lines(v)
    adj = defaultdict(list)
    R, C = len(G), len(G[0])
    test = 0
    for x in range(R):
        for y in range(C):
            ch = G[x][y]
            if ch == '#': continue
            for d in range(4):
                for d2, (dx, dy) in enumerate(DIRS):
                    adj[x, y, d]
                    if (d2 - d)%4 == 2: continue # walk to parent
                    nx, ny = dx+x, dy+y
                    if 0 <= nx < R and 0 <= ny < C and testDir(d2, G[nx][ny]):
                        adj[x,y,d].append((nx, ny, d2))

    return solve(adj, G)

def p2(v):
    G = get_lines(v)
    adj = defaultdict(list)
    R, C = len(G), len(G[0])
    for x in range(R):
        for y in range(C):
            ch = G[x][y]
            if ch == '#': continue
            for d in range(4):
                for d2, (dx, dy) in enumerate(DIRS):
                    if (d2 - d)%4 == 2: continue # walk to parent
                    nx, ny = dx+x, dy+y
                    if 0 <= nx < R and 0 <= ny < C and G[nx][ny] != '#':
                        adj[x,y,d].append((nx, ny, d2))
    return solve(adj, G)


if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
