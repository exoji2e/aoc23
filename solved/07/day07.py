#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 7
def get_year(): return 2023

def parse(ln):
    c, b = ln.split()
    return [c, int(b)]

def is5(cds):
    C = Counter(cds)
    return max(C.values()) == 5

def is4(cds):
    C = Counter(cds)
    return max(C.values()) == 4

def isFH(cds):
    C = Counter(cds)
    return len(C) == 2 and max(C.values()) == 3

def is3(cds):
    C = Counter(cds)
    return max(C.values()) == 3

def pair2(cds):
    C = Counter(cds)
    x = list(C.values())
    c2 = Counter(x)
    return c2[2] == 2

def pair(cds):
    C = Counter(cds)
    return max(C.values()) == 2

def fsc(cds):
    if is5(cds): return 10
    if is4(cds): return 9
    if isFH(cds): return 8
    if is3(cds): return 7
    if pair2(cds): return 6
    if pair(cds): return 5
    return 4

def cSc(c):
    return cardScore[c]

def score(hand):
    cards = hand[0]
    lst = [fsc(cards)]
    for c in cards:
        lst.append(cSc(c))
    return tuple(lst)

CARDS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'T', 'J', 'Q', 'K', 'A']
cardScore = {str(k) : i for i, k in enumerate(CARDS)}

def score2(hand):
    cards = hand[0]
    best = 0
    for c in cards:
        t = cards.replace('J', str(c))
        best = max(best, fsc(t))

    lst = [best]
    for c in cards.replace('J', '1'):
        lst.append(cSc(c))
    return tuple(lst)



def p1(v):
    lns = get_lines(v)
    ans = 0
    hands = []
    for ln in lns:
        hands.append(parse(ln))
    hands.sort(key=score)
    for i, (h, bet) in enumerate(hands):
        ans += (i+1)*bet

    return ans

def p2(v):
    lns = get_lines(v)
    ans = 0
    hands = []
    for ln in lns:
        hands.append(parse(ln))
    hands.sort(key=score2)
    for i, (h, bet) in enumerate(hands):
        ans += (i+1)*bet

    return ans


if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
