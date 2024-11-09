import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(start) -> int:
  q = deque([(start[0], start[1])])
  matrix[start[0]][start[1]] = 0
  count = 1

  while q:
    now_r, now_c= q.popleft()
    for d in range(4):
      next_r, next_c = now_r + dx[d], now_c + dy[d]

      if not( 0 <= next_r < row and 0<= next_c < col ):
        continue

      if matrix[next_r][next_c] == 1:
        matrix[next_r][next_c] = 0
        q.append((next_r, next_c))
        count += 1
    
  return count

row, col = map(int, input().split())

matrix = []
for _ in range(row):
  line = list(map(int, input().split()))
  matrix.append(line)

biggest_picture = 0
number_of_picture = 0

for r in range(row):
  for c in range(col):
    if matrix[r][c] == 1:
      size_of_picture = bfs((r, c))
      biggest_picture = max(biggest_picture, size_of_picture)
      number_of_picture += 1

print(number_of_picture)
print(biggest_picture)