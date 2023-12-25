#!/usr/bin/python3
import sys, time, datetime
sys.path.extend(['..', '.'])
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 25
def get_year(): return 2023


# used in mincut @ Kattis
from collections import defaultdict
class Flow:
    def __init__(self, sz):
        self.G = [
            defaultdict(int) for _ in range(sz)
        ] # neighbourhood dict, N[u] = {v_1: cap_1, v_2: cap_2, ...}
        self.Seen = set() # redundant

    def increase_capacity(self, u, v, cap):
        """ Increases capacity on edge (u, v) with cap.
            No need to add the edge """
        self.G[u][v] += cap

    def max_flow(self, source, sink):
        def dfs(u, hi):
            G = self.G
            Seen = self.Seen
            if u in Seen: return 0
            if u == sink: return hi

            Seen.add(u)
            for v, cap in G[u].items():
                if cap >= self.min_edge:
                    f = dfs(v, min(hi, cap))
                    if f:
                        G[u][v] -= f
                        G[v][u] += f
                        return f
            return 0

        flow = 0
        self.min_edge = 2**30 # minimal edge allowed
        while self.min_edge > 0:
            self.Seen = set()
            pushed = dfs(source, float('inf'))
            if not pushed:
                self.min_edge //= 2
            flow += pushed
        return flow, self.Seen

def parse(ln):
    return multi_split(ln, ' :')


def buildBaseNet(N, edgs):
    net = Flow(N + 2)
    for i, j in edgs:
        net.increase_capacity(i, j, 1)
        net.increase_capacity(j, i, 1)
    return net

def p1(v):
    lns = get_lines(v)
    edgs = []
    nodes = {}
    for ln in lns:
        item = parse(ln)
        for a in item:
            if a not in nodes:
                nodes[a] = len(nodes)

        i1 = nodes[item[0]]
        for b in item[1:]:
            i2 = nodes[b]
            edgs.append((i1, i2))
    N = len(nodes)
    S, T = N, N+1
    for endIdx in range(1, S):
        net = buildBaseNet(N, edgs)
        net.increase_capacity(S, 0, 4)
        net.increase_capacity(endIdx, T, 4)
        f, seen = net.max_flow(S, T)
        if f == 3:
            ls = len(seen) - 1
            return ls*(len(nodes) - ls)
    return 'no solution found'

def p2(v):
    return 'Push The Big Red Button!'


if __name__ == '__main__':
    options = get_commands()
    print('Commands:', options)
    main(get_year(), get_day(), p1, p2, options, FILE=__file__)
