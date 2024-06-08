import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input())
start, end = map(int,input().split())
m = int(input())
graph = defaultdict(list)

for _ in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

def bfs(start_v, target_v):
  queue = deque([])
  queue.append((start_v, 0))
  visited = set()

  while queue:
    current_v, count = queue.popleft()
    if current_v == target_v:
      return count
    for next_v in graph[current_v]:
      if next_v not in visited:
        visited.add(next_v)
        queue.append((next_v, count+1 ))
  
  return -1

print(bfs(start, end))