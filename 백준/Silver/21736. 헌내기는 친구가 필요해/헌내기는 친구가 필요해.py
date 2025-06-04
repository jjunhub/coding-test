from collections import deque
START_POSITION, PERSON, WALL = "I", "P", "X"

N, M = map(int, input().split())

matrix = []
for row in range(N):
  line = input()
  for col in range(M):
    if line[col] == START_POSITION:
      start = (row, col)
      break
  matrix.append(line)

q = deque()
q.append(start)
visited = set()
visited.add(start)
answer = 0
dir = [ (0, 1), (0, -1), (1, 0), (-1, 0) ]

while q:
  cur_row, cur_col = q.popleft()
  if matrix[cur_row][cur_col] == PERSON:
    answer += 1
  
  for dr, dc in dir:
    next_row = cur_row + dr
    next_col = cur_col + dc

    if not (0 <= next_row < N and 0 <= next_col < M):
      continue

    if (next_row, next_col) not in visited:
      if matrix[next_row][next_col] != WALL:
        visited.add((next_row, next_col))
        q.append((next_row, next_col))

if answer == 0:
  print("TT")
else:
  print(answer)