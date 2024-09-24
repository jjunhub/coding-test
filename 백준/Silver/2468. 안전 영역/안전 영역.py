from collections import deque
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(row, column, visited:set):
  q = deque([(row, column)])
  visited.add((row, column))

  while q:
    cur_row, cur_column = q.popleft()

    for d in range(4):
      next_row, next_column = cur_row + dir[d][0], cur_column + dir[d][1]

      if not ( 0 <= next_row < N and 0 <= next_column < N):
        continue
    
      if (next_row, next_column) not in visited and matrix[next_row][next_column] > 0:
        visited.add((next_row, next_column))
        q.append((next_row, next_column))


N = int(input())
matrix = []
for _ in range(N):
  matrix.append(list(map(int, input().split())))

answer = 1
for water_height in range(1, 101):
  safety_area = 0
  visited = set()
  for row in range(N):
    for column in range(N):
      matrix[row][column] -= 1
  
  for row in range(N):
    for column in range(N):
      if matrix[row][column] > 0 and (row, column) not in visited:
        bfs(row, column, visited)
        safety_area += 1
  
  answer = max(answer, safety_area)
  if safety_area == 0:
    break

print(answer)