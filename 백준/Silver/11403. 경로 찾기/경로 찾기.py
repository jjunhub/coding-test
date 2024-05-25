from collections import deque, defaultdict
import sys
input = sys.stdin.readline

N = int(input())
graph = defaultdict(list)

for i in range(N):
  route = list(map(int, input().split()))
  for start, end in enumerate(route):
    if end == 0 : continue
    graph[i].append(start)

def bfs(start_v):
  visited = set()
  queue = deque([])
  queue.append(start_v)
  while queue:
    cur_v = queue.popleft()
    for v in graph[cur_v]:
      if v not in visited:
        visited.add(v)
        queue.append(v)
  
  return visited

answer = [ ]

for start_v in range(N):
  result = bfs(start_v)
  temp = [0] * N
  for idx in result:
    temp[idx] = 1
  answer.append(temp)

for row in answer:
  print(*row)