from collections import defaultdict

N = int(input())
pair = int(input())
graph = defaultdict(list)
visited = set()

def dfs(v):
  visited.add(v)
  for next_v in graph[v]:
    if next_v not in visited:
      dfs(next_v)

for _ in range(pair):
  v1, v2 = map(int, input().split())
  graph[v1].append(v2)
  graph[v2].append(v1)

dfs(1)
print(len(visited)-1)