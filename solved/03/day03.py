#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 3
def get_year(): return 2023

def p1(v):
    lns = get_lines(v)
    ans = 0
    def isSymbol(letter):
        return not ('0' <= letter <= '9') and letter != '.'
    R = len(lns)
    for i, row in enumerate(lns):
        C = len(row)
        poss = []
        curr = []
        for j, letter in enumerate(row):
            if '0' <= letter <= '9':
                if curr and curr[-1] != j-1:
                    poss.append(curr)
                    curr = []
                curr.append(j)
        if curr: poss.append(curr)
        for arr in poss:
            no = int(''.join(row[x] for x in arr))
            ok = False
            for j in arr:
                for ni, nj in grid8nf(i, j, R, C):
                    if isSymbol(lns[ni][nj]):
                        ok = True
            if ok:
                ans += no
    return ans

def p2(v):
    lns = get_lines(v)
    ans = 0
    R = len(lns)
    C2IDX = {}
    NUMBERS = []
    for i, row in enumerate(lns):
        C = len(row)
        poss = []
        curr = []
        for j, letter in enumerate(row):
            if '0' <= letter <= '9':
                if curr and curr[-1] != j-1:
                    poss.append(curr)
                    curr = []
                curr.append(j)
        if curr: poss.append(curr)
        for arr in poss:
            no = int(''.join(row[x] for x in arr))
            idx = len(NUMBERS)
            NUMBERS.append(no)
            for j in arr:
                C2IDX[i,j] = idx

    for i, row in enumerate(lns):
        C = len(row)
        for j, letter in enumerate(row):
            if letter == '*':
                ids = set()
                for T in grid8nf(i, j, R, C):
                    if T in C2IDX:
                        ids.add(C2IDX[T])
                nos = [NUMBERS[idx] for idx in ids]
                if len(nos) == 2:
                    ans += nos[0]*nos[1]
    return ans


if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
