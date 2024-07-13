import sys
from collections import deque
input = sys.stdin.readline

def bfs(start_list) -> int:
  queue = deque()
  queue.extend(start_list) # [ ((h1,y1), 0), ... ]
  max_day = -1

  while queue:
    point, day = queue.popleft()
    max_day = max(day, max_day)
    dx = [0, 0, -1, 1] # 상 하 좌 우
    dy = [1, -1, 0, 0]
    h, y = point

    for direction in range(4):
      next_h, next_y = ( h + dy[direction], y + dx[direction])
      if 0 <= next_h < hang and 0 <= next_y < yeol:
        if matrix[next_h][next_y] == 0:
          matrix[next_h][next_y] = 1
          next = (next_h, next_y)
          queue.append((next, day+1))
  return max_day

def check_any_tomato_not_ripen() -> bool:
  for h in range(hang):
    for y in range(yeol):
      if matrix[h][y] == 0:
        return True
  return False

def find_tomato_locations() -> list:
  start_list = []
  for h in range(hang):
    for y in range(yeol):
      if matrix[h][y] == 1:
        start_list.append(((h,y),0))
  return start_list

yeol, hang = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(hang)]
max_day = bfs(find_tomato_locations())

if check_any_tomato_not_ripen() :
  print(-1)
else :
  print(max_day)