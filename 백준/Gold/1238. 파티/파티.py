from collections import defaultdict
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dijkstra(start_node, end_node):
  visited = set()
  q = list()
  heappush(q, (0, start_node))

  while q:
    total_cost, now_node = heappop(q)
    if now_node == end_node:
      return total_cost
    
    if now_node in visited:
      continue
    visited.add(now_node)

    for next_node, cost in graph[now_node]:
      if next_node not in visited:
        heappush(q, (total_cost+cost, next_node))

graph = defaultdict(list)
node_number, edge_number, party_node = map(int, input().split())
for _ in range(edge_number):
  start_node, end_node, cost = map(int, input().split())
  graph[start_node].append((end_node, cost))

answer = -1
for home_node in range(1, node_number+1):
  answer = max(answer, dijkstra(home_node, party_node) + dijkstra(party_node, home_node))

print(answer)