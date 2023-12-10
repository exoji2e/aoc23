#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 10
def get_year(): return 2023

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

def solve(S, lns):
    R = len(lns)
    C = len(lns[0])
    q = [S]
    vis = set(q)
    i = -1
    foundS = []
    path = [S]
    while q:
        q2 = []
        for x, y in q:
            ch = lns[x][y]
            nbs = []
            if ch == '|':
                nbs = [(x-1, y), (x+1, y)]
            elif ch == '-':
                nbs = [(x, y - 1), (x, y+1)]
            elif ch == 'L':
                nbs = [(x-1, y), (x, y+1)]
            elif ch == 'J':
                nbs = [(x-1, y), (x, y - 1)]
            elif ch == '7':
                nbs = [(x+1, y), (x, y - 1)]
            elif ch == 'F':
                nbs = [(x+1, y), (x, y + 1)]
            for nx, ny in nbs:
                if lns[nx][ny] == 'S': foundS.append(i)
                elif (nx, ny) not in vis:
                    vis.add((nx, ny))
                    q2.append((nx, ny))
                    path.append((nx, ny))
        q = q2
        i += 1
    return -1 in foundS, i, path




def solvePath(path):

    DD = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    def rotate(dx, dy):
        i = DD.index((dx, dy))
        return DD[i-1], DD[(i+1)%4]

    def getL(coords):
        (x1, y1), (x2, y2), (x3, y3) = coords
        dx, dy = x2 - x1, y2 - y1
        dx2, dy2 = x3 - x2, y3 - y2
        dl, dr = rotate(dx, dy)
        dl2, dr2 = rotate(dx2, dy2)
        xL, yL = x2 + dl[0], y2 + dl[1]
        xL2, yL2 = x2 + dl2[0], y2 + dl2[1]
        return [(xL, yL), (xL2, yL2)]

    def getR(coords):
        (x1, y1), (x2, y2), (x3, y3) = coords
        dx, dy = x2 - x1, y2 - y1
        dx2, dy2 = x3 - x2, y3 - y2
        dl, dr = rotate(dx, dy)
        dl2, dr2 = rotate(dx2, dy2)
        xL, yL = x2 + dr[0], y2 + dr[1]
        xL2, yL2 = x2 + dr2[0], y2 + dr2[1]
        return [(xL, yL), (xL2, yL2)]
    X = set(path)
    left = []
    right = []
    for i in range(len(path)):
        coords = [path[i-1], path[i], path[(i+1)%len(path)]]
        nl = getL(coords)
        left.extend(nl)
        nr = getR(coords)
        right.extend(nr)
    print(max(left), max(right))
    use = left if max(left) < max(right) else right
    q = [t for t in set(use) if t not in X]
    vis = set(q)
    for x, y in q:
        for T in grid4n(x, y):
            if T not in X and T not in vis:
                vis.add(T)
                q.append(T)
    return len(vis)

def solveArea(path):
    def area2(cords):
        A = 0
        for i in range(len(cords)):
            A += (cords[i-1][0] + cords[i][0]) * (cords[i-1][1] - cords[i][1])
        return abs(A)

    a2 = area2(path)
    ans = (a2 - len(path) + 2)//2
    return ans

def findS(lns):
    for i, ln in enumerate(lns):
        for j, ch in enumerate(ln):
            if ch == 'S':
                return i, j

def p1(v):
    lns = get_lines(v)
    sx, sy = findS(lns)
    for nx, ny in grid4n(sx, sy):
        ok, _, path = solve((nx, ny), lns)
        if ok: break
    path.append((sx, sy))

    return len(path)//2

def p2(v):
    lns = get_lines(v)
    sx, sy = findS(lns)
    for nx, ny in grid4n(sx, sy):
        ok, _, path = solve((nx, ny), lns)
        if ok: break
    path.append((sx, sy))

    return solveArea(path)


if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
