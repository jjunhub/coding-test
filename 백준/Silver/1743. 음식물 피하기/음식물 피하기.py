from collections import deque
mv = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(r, c):
  q = deque()
  q.append((r,c))
  food_size = 0
  matrix[r][c] = 0

  while q:
    now_r, now_c = q.popleft()
    food_size += 1

    for dr, dc in mv:
      next_r = now_r + dr
      next_c = now_c + dc
      if not (0 <= next_r < N and 0 <= next_c < M):
       continue

      if matrix[next_r][next_c] == 1:
        matrix[next_r][next_c] = 0
        q.append((next_r, next_c))
  return food_size

N, M, K = map(int, input().split())
matrix = [[ 0 for _ in range(M)] for _ in range(N)]
max_food_size = 0

for _ in range(K):
  r, c = map(int, input().split())
  matrix[r-1][c-1] = 1
  
for r in range(N):
    for c in range(M):
      if matrix[r][c] == 1:
        max_food_size = max(max_food_size, bfs(r, c))

print(max_food_size)