import sys
from collections import defaultdict
from heapq import heappop, heappush
input = sys.stdin.readline
FAIL =  200000 * 1000

def dijkstra(start_v, end_v) -> int:
  visited = set()
  heapq = list()
  heappush(heapq, (0, start_v))

  while heapq:
    current_cost, current_v = heappop(heapq)
    if current_v in visited:
      continue
    visited.add(current_v)

    if current_v == end_v:
      return current_cost

    for next_cost, next_v in graph[current_v]:
      if next_v not in visited:
        heappush(heapq, (next_cost + current_cost, next_v))
  return FAIL

N, E = map(int, input().split())
graph = defaultdict(list)

for _ in range(E):
  start_v, end_v, cost = map(int ,input().split())
  graph[start_v].append((cost, end_v))
  graph[end_v].append((cost, start_v))

v1, v2 = map(int, input().split())
result = FAIL

# case 1 : 1 -> v1 -> v2 -> N
path1 = dijkstra(1, v1)
path2 = dijkstra(v1, v2)
path3 = dijkstra(v2, N)
result = min(result, path1+path2+path3)

# case 2 : 1 -> v2 -> v1 -> N
path1 = dijkstra(1, v2)
# path2 = dijkstra(v2, v1)
path3 = dijkstra(v1, N)
result = min(result, path1+path2+path3)

if result >= FAIL:
  print("-1")
else:
  print(result)