#!/usr/bin/env python3

from sys import stdin
from typing import Dict
from parse import parse


def solve(starting_point: str = 'AA', graph: Dict = {}):
    # print(graph)
    nonzero = list(filter(lambda x: graph[x]['flow_rate'] > 0, graph))
    # dp[i][k][j] = maximum amount of pressure released at minute i, standing at
    #           location k, with the valves marked in bitset j opened
    dp = [[[-99999999 for k in range(1 << len(nonzero))]
           for j in range(len(nonzero))] for i in range(31)]
    prev = [[[[-1, -1, -1] for k in range(1 << len(nonzero))]
             for j in range(len(nonzero))] for i in range(31)]

    for i, node in enumerate(nonzero):
        dist = graph[starting_point]['dist'][node]
        dp[dist + 1][i][1 << i] = 0
        # print("base", dist + 1, i, 1 << i, node)

    def get_flow(mask: int):
        ans = 0
        for i, node in enumerate(nonzero):
            if ((1 << i) & mask) != 0:
                ans += graph[node]['flow_rate']
        return ans

    part_1 = 0
    for i in range(1, 31):
        for j in range(1 << len(nonzero)):
            for k, curr in enumerate(nonzero):
                flow = get_flow(j)

                hold = dp[i-1][k][j] + flow
                if hold > dp[i][k][j]:
                    dp[i][k][j] = hold
                    prev[i][k][j] = [i-1, k, j]

                part_1 = max(part_1, dp[i][k][j])
                if ((1 << k) & j) == 0:
                    # print(k, "not in", j)
                    continue

                for l, next_node in enumerate(nonzero):
                    if ((1 << l) & j) != 0:
                        # print(l, "already in", j, "|", i, k)
                        continue

                    # distance from curr to next_node
                    dist = graph[curr]['dist'][next_node]
                    if(i+dist+1 >= 31):
                        continue
                    # print(i, k, j, "->", i + dist + 1, l, j | (1 << l),
                    #   dp[i + dist + 1][l][j | (1 << l)], dp[i][k][j] + (flow * (dist + 1)))
                    value = dp[i][k][j] + (flow * (dist + 1))
                    if value > dp[i + dist + 1][l][j | (1 << l)]:
                        dp[i + dist + 1][l][j | (1 << l)] = value
                        prev[i + dist + 1][l][j | (1 << l)] = [i, k, j]
    part_2 = 0
    for i in range(1 << len(nonzero)):
        for j in range(1 << len(nonzero)):
            if i & j != j:
                continue

            a, b = -999999, -999999
            for k in range(len(nonzero)):
                a = max(a, dp[26][k][j])
                b = max(b, dp[26][k][i & ~j])
            part_2 = max(part_2, a+b)
    return part_1, part_2


if __name__ == '__main__':
    graph = {}
    input = stdin.readlines()
    for line in input:
        result = parse(
            "Valve {} has flow rate={}; tunnels lead to valves {}", line)
        if not result:
            result = parse(
                "Valve {} has flow rate={}; tunnel leads to valve {}", line)
        valve, rate, connections = result
        graph[valve] = {"flow_rate": int(
            rate), "adj": connections.strip().split(', ')}

    for vertex in graph:
        q = [vertex]
        dist = {vertex: 0}
        seen = {vertex}
        while q:
            name = q.pop(0)
            for neighbour in graph[name]['adj']:
                if neighbour not in seen:
                    seen.add(neighbour)
                    dist[neighbour] = dist[name] + 1
                    q.append(neighbour)

        graph[vertex]['dist'] = dist
    print(solve(graph=graph))
