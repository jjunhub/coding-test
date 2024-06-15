import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = defaultdict(list)
visitedRoute = [0] * (N+1)
visited = set()
ans = 1

for _ in range(M):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

for key in graph:
  graph[key].sort()

def dfs(v):
  global ans

  visited.add(v)
  visitedRoute[v] = ans
  for next_v in graph[v]:
    if next_v not in visited:
      ans += 1
      dfs(next_v)
  return

dfs(R)

for v in visitedRoute[1:]:
  print(v)