from collections import defaultdict
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dijkstra(start, end):
  visited = set()
  q = list()
  heappush(q , (0, start)) # cost, node, total_cost

  while q:
    total_cost, now_node = heappop(q)
    if now_node in visited:
      continue

    visited.add(now_node)
    if now_node == end:
      return total_cost

    for next_node, cost in graph[now_node]:
      if next_node not in visited:
        heappush(q, (total_cost + cost, next_node))

node, edge = map(int, input().split())
graph = defaultdict(list)

for _ in range(edge):
  node1, node2, cost = map(int, input().split())
  graph[node1].append((node2, cost))
  graph[node2].append((node1, cost))

print(dijkstra(1, node))