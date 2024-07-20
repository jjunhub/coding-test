import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def bfs(start_v):
  q = deque()
  q.append(start_v)
  visited.add(start_v)
  
  while q:
    now_v = q.popleft()
    for next_v in graph[now_v]:
      if next_v not in visited:
        visited.add(next_v)
        q.append(next_v)

N, M = map(int, input().split())
graph = defaultdict(list)
visited = set()
cc = 0

for _ in range(M):
  v1, v2 = map(int, input().split())
  graph[v1].append(v2)
  graph[v2].append(v1)


for v in range(1,N+1):
  if v not in visited:
    bfs(v)
    cc += 1

print(cc)