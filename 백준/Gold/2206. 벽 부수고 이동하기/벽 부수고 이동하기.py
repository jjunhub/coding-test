import sys
from collections import deque
input = sys.stdin.readline
INF = 1000000000

def bfs(start_row, start_column) -> int:
  visited = [[[ INF for count in range(2)] for column in range(column_number)] for row in range(row_number)]
  # visited[row][column][0] is distance that dosen't use power, and [1] use power.

  q = deque()
  q.append((start_row, start_column, False, 1))
  move = [ (0, 1), (0, -1), (1, 0), (-1, 0) ]

  while q:
    now_row, now_column, is_use_power, distance = q.popleft()

    if visited[now_row][now_column][is_use_power] <= distance:
      continue
    visited[now_row][now_column][is_use_power] = distance

    for row_mv, col_mv in move:
      next_row, next_column = now_row + row_mv, now_column + col_mv
      if not (0 <= next_row < row_number and 0 <= next_column < column_number):
        continue

      if matrix[next_row][next_column] == '1': # next step is wall
        if not (is_use_power == True) and visited[next_row][next_column][1] > distance+1:
          q.append((next_row, next_column, True, distance+1))
          
      else:
        if visited[next_row][next_column][is_use_power] <= distance+1:
          continue
        q.append((next_row, next_column, is_use_power, distance+1))
  
  result = min(visited[row_number-1][column_number-1])
  if result == INF:
    return -1
  else :
    return result

      
row_number, column_number = map(int, input().split())
matrix = list()
for _ in range(row_number):
  matrix.append(list(input().rstrip()))

print(bfs(0,0))  