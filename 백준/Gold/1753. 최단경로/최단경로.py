import sys
from collections import defaultdict
from heapq import heapify, heappop, heappush
input = sys.stdin.readline

def dijkstra(start):
  q = [(0, start)]
  heapify(q)

  while q:
    now_weight, now_vertex = heappop(q)
    if visited[now_vertex] != -1:
      continue
    visited[now_vertex] = now_weight

    for next_weight, next_vertex in graph[now_vertex]:
      if visited[next_vertex] == -1:
        heappush(q, (now_weight + next_weight, next_vertex))

V, E = map(int,input().split())
start = int(input())
graph = defaultdict(list)
visited = [-1] * (V+1)

for _ in range(E):
  start_v, end_v, weight = map(int, input().split())
  graph[start_v].append((weight, end_v))

dijkstra(start)

for w in visited[1:]:
  answer = w if w != -1 else "INF"
  print(answer)