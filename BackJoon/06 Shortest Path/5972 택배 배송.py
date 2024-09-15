'''
택배 배송

- 다익스트라 알고리즘
'''

import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
roads = list(list(map(int, input().split())) for _ in range(m))
prices = list(1e9 for _ in range(n+1))

graph = list([] for _ in range(n+1))
for road in roads:
    graph[road[0]].append([road[1], road[2]]) # 목적지, 여물 비용
    graph[road[1]].append([road[0], road[2]])

def dijikstra(start):
    q = []
    heapq.heappush(q, (0, start))
    prices[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if prices[now] < dist:
            continue
        for item in graph[now]:
            cost = dist + item[1]
            if prices[item[0]] > cost:
                heapq.heappush(q, (cost, item[0]))
                prices[item[0]] = cost

dijikstra(1)
print(prices[-1])
