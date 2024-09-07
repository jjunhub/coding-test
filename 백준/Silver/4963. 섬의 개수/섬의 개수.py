from collections import deque
import sys
input = sys.stdin.readline

def bfs(h, w):
  q = deque([(h, w)])
  mv = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

  while q:
    now_h, now_w = q.popleft()

    for i in range(8):
      next_h, next_w = now_h + mv[i][0], now_w + mv[i][1]

      if not (0 <= next_h < height and 0 <= next_w < width) :
         continue
      
      if matrix[next_h][next_w] == 1:
        matrix[next_h][next_w] = 0
        q.append((next_h, next_w))

while True:
  width, height = map(int, input().split())
  if width == 0 and height == 0:
    break

  matrix = []
  island_number = 0
  for _ in range(height):
    matrix.append(list(map(int, input().split())))
  
  for h in range(height):
    for w in range(width):
      if matrix[h][w] == 1:
        matrix[h][w] = 0
        bfs(h, w)
        island_number += 1
  
  print(island_number)