from collections import deque

N = int(input())
matrix_n = [] # for normal
matrix_rg = [] # for red-green

for _ in range(N):
  one_row = input()
  matrix_n.append(list(one_row))

  one_row_changed = list(one_row)
  for idx in range(len(one_row_changed)):
    if one_row_changed[idx] == "G":
      one_row_changed[idx] = "R"
  matrix_rg.append(one_row_changed)

def bfs(start_r : int, start_c : int, rg_status : bool):
  target = matrix_rg if rg_status else matrix_n
  
  q = deque([(start_r, start_c, target[r][c])])
  target[r][c] = "X"
  mv = [ (1, 0), (-1, 0), (0, -1), (0, 1) ]
  
  while q :
    rows, columns, now_zone = q.popleft()

    for i in range(4):
      next_rows, next_columns = rows + mv[i][0], columns + mv[i][1]
      if not ( 0 <= next_rows < N and 0 <= next_columns < N) :
        continue
      
      if target[next_rows][next_columns] == now_zone:
          target[next_rows][next_columns] = "X"
          q.append((next_rows, next_columns, now_zone))

answer = []
for status in (False, True):
  target = matrix_rg if status else matrix_n
  count = 0
  for r in range(N):
    for c in range(N):
      if target[r][c] != "X":
        bfs(r,c, status)
        count += 1
  answer.append(count)

print(*answer)