from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
# N is y, M is x

miro = [ [ ] for _ in range(N)]

for y in range(N):
  garo = input().rstrip()
  for val in garo:
    miro[y].append(int(val))

def bfs(start_v):
  visited = set()
  visited.add(start_v)
  q = deque([])
  q.append((start_v, 1))

  while q :
    cur_v, distance = q.popleft()
    x, y = cur_v

    if x == N - 1 and y == M - 1:
      return distance
    
    # 상
    if y+1 < M and (x, y+1) not in visited and miro[x][y+1] == 1:
      q.append(((x, y+1), distance + 1))
      visited.add((x, y+1))
    
    # 하
    if y-1 >= 0 and (x, y-1) not in visited and miro[x][y-1] == 1:
      q.append(((x, y-1), distance + 1))
      visited.add((x, y-1))

    # 좌
    if x-1 >= 0 and (x-1, y) not in visited and miro[x-1][y] == 1:
      q.append(((x-1,y), distance + 1))      
      visited.add((x-1,y))

    if x+1 < N and (x+1, y) not in visited and miro[x+1][y] == 1:
      q.append(((x+1,y), distance + 1))      
      visited.add((x+1, y))

print(bfs((0,0)))