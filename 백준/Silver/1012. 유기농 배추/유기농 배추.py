import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
  q = deque()
  q.append(start)
  dir = [(1, 0), (-1, 0), (0, -1), (0, 1)] # 상하좌우

  while q:
    now_v = q.popleft() # (h, y)
    
    for i in range(4):
      next_h, next_y = (now_v[0]+dir[i][0], now_v[1]+dir[i][1])
      
      if not (0 <= next_h < hang and 0 <= next_y < yeol):
        continue

      if matrix[next_h][next_y] == 1:
        matrix[next_h][next_y] = 0
        q.append((next_h, next_y))
  
T = int(input())
for _ in range(T):
  yeol, hang, K = map(int, input().split())
  matrix = [[ 0 for i in range(yeol)] for j in range(hang)]
  earthwarm = 0

  for _ in range(K):
    y, h = map(int, input().split())
    matrix[h][y] = 1
  
  for h in range(hang):
    for y in range(yeol):
      if matrix[h][y] == 1:
        bfs((h,y))
        earthwarm += 1
  
  print(earthwarm)