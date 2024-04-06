from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
dct = defaultdict(list)
dfsVisited = []

for _ in range(M):
  V1, V2 = map(int,input().split())
  dct[V1].append(V2)
  dct[V2].append(V1)

for v in dct.keys():
  dct[v].sort()

def bfs(V):
  visited = [V]
  q = deque([])
  q.append(V)

  while q:
    cur_v = q.popleft()
    for v in dct[cur_v]:
      if v not in visited:
        visited.append(v)
        q.append(v)
  return visited

def dfs(V):
  dfsVisited.append(V)
  for next_v in dct[V]:
    if next_v not in dfsVisited:
      dfs(next_v)

dfs(V)
print(*dfsVisited)
print(*bfs(V))