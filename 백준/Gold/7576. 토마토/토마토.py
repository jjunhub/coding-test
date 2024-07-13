import sys
from collections import deque
input = sys.stdin.readline

yeol, hang = map(int, input().split())
matrix = list()
visited = [ [False] * yeol for _ in range(hang)]

for _ in range(hang):
  line = list(map(int, input().split()))
  matrix.append(line)

def bfs(start_list) -> int:
  queue = deque()
  queue.extend(start_list) # ((h,y), 0)
  max_day = -1
  while queue:
    point, day = queue.popleft()
    max_day = max(day, max_day)
    dx = [0, 0, -1, 1] # 상 하 좌 우
    dy = [1, -1, 0, 0]
    h, y = point

    for direction in range(4):
      next_h, next_y = ( h + dy[direction], y + dx[direction])
      if next_h < 0 or next_h >= hang or next_y < 0 or next_y >= yeol:
        continue
      else :
        if visited[next_h][next_y] == False and matrix[next_h][next_y] == 0 :
          visited[next_h][next_y] = True
          next = (next_h, next_y)
          queue.append((next, day+1))
  return max_day


start_list = []
for h in range(hang):
  for y in range(yeol):
    if matrix[h][y] == 1:
      visited[h][y] = True
      start_list.append(((h,y),0))
    elif matrix[h][y] == -1:
      visited[h][y] = True

max_day = bfs(start_list)

flag = True
for h in range(hang):
  if False in visited[h] :
      flag = False

if flag :
  print(max_day)
else :
  print(-1)