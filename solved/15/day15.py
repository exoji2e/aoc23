#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 15
def get_year(): return 2023

def parse(ln):
    return lazy_ints(multi_split(ln, ' '))

def hash(s):
    v = 0
    for ch in s:
        v += ord(ch)
        v *= 17
        v %= 256
    return v

def getWordOp(item):
    x = next(i for (i, ch) in enumerate(item) if not 'a' <= ch <= 'z')
    return item[:x], item[x:]

def p1(v):
    ans = 0
    items = v.split(',')
    boxes = defaultdict(list)
    for s in items:
        ans += hash(s)
    return ans

def p2(v):
    ans = 0
    items = v.split(',')
    boxes = defaultdict(list)
    for s in items:
        w, op = getWordOp(s)
        h = hash(w)
        if op == '-':
            boxes[h] = list(filter(lambda lens: lens[0] != w, boxes[h]))
        else:
            f = int(op[1:])
            found = False
            for i in range(len(boxes[h])):
                if boxes[h][i][0] == w:
                    boxes[h][i] = (w, f)
                    found = True
            if not found:
                boxes[h].append((w, f))
    for k, v in boxes.items():
        for i, (_, f) in enumerate(v):
            ans += (k+1)*(i+1)*f
    return ans


if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
