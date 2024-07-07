import sys, heapq
from collections import defaultdict

input = sys.stdin.readline

N = int(input()) # Node
M = int(input()) # Edge

graph = defaultdict(list)

for _ in range(M):
  s, e, weight = map(int, input().split())
  graph[s].append((e, weight))

start, end = map(int, input().split())

def dijkstra(start, end) -> int:
  cost = { }
  pq = [ ]
  heapq.heappush(pq, (0, start))

  while pq:
    weight, current_node = heapq.heappop(pq)
    if current_node not in cost:
      cost[current_node] = weight
      for next_node, next_weight in graph[current_node]:
        heapq.heappush(pq, (weight + next_weight, next_node))
  
  return cost[end]

print(dijkstra(start, end))
