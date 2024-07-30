from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
  q = deque()
  q.append((start[0], start[1], 0))
  matrix[start[0]][start[1]] = 0
  matrix_visited[start[0]][start[1]] = True
  move = [ (1, 0), (-1, 0), (0, -1), (0, 1)]

  while q:
    now_hang, now_yeol, distance = q.popleft()

    for dir in range(4): # 상 하 좌 우
      next_hang = now_hang + move[dir][0]
      next_yeol = now_yeol + move[dir][1]

      if not (0 <= next_hang < hang and 0 <= next_yeol < yeol):
        continue

      if not matrix_visited[next_hang][next_yeol]:
        matrix[next_hang][next_yeol] = distance + 1
        matrix_visited[next_hang][next_yeol] = True
        q.append((next_hang, next_yeol, distance + 1))

matrix = []
hang, yeol = map(int, input().split())
matrix_visited = [ [False] * yeol for _ in range(hang) ]

for h in range(hang):
  row = list(map(int, input().split()))
  for y, el in enumerate(row):
    if el == 2:
      target = (h, y)
    elif el == 0:
      matrix_visited[h][y] = True  
  matrix.append(row)

bfs(target)

for h in range(hang):
  for y in range(yeol):
    if matrix_visited[h][y] == False:
      matrix[h][y] = -1

for h in range(hang):
  print(*matrix[h])