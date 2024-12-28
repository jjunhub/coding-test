from itertools import combinations

def find_max_candy():
  max_candy = 0

  # 가로 체크
  for row_idx in range(N):
    before_val = -1
    count = 1
    for col_idx in range(N):
      cur_val = matrix[row_idx][col_idx]
      if before_val == cur_val:
        count += 1
      else :
        count = 1
      before_val = cur_val
      max_candy = max(max_candy, count)

  # 세로 체크
  for col_idx in range(N):
    before_val = -1
    count = 1
    for row_idx in range(N):
      cur_val = matrix[row_idx][col_idx]
      if before_val == cur_val:
        count += 1
      else :
        count = 1
      before_val = cur_val
      max_candy = max(max_candy, count)

  # 세로 따지기
  return max_candy


N = int(input())
matrix = []
for _ in range(N):
  matrix.append(list(input()))

max_candy = -1
for row_idx in range(N):
  for col_idx in range(N):
    # 오른쪽
    if col_idx + 1 < N:
      matrix[row_idx][col_idx], matrix[row_idx][col_idx+1] = matrix[row_idx][col_idx+1], matrix[row_idx][col_idx]
      max_candy = max(max_candy, find_max_candy())
      matrix[row_idx][col_idx], matrix[row_idx][col_idx+1] = matrix[row_idx][col_idx+1], matrix[row_idx][col_idx]

    # 아래
    if row_idx + 1 < N:
      matrix[row_idx][col_idx], matrix[row_idx+1][col_idx] = matrix[row_idx+1][col_idx], matrix[row_idx][col_idx]
      max_candy = max(max_candy, find_max_candy())
      matrix[row_idx][col_idx], matrix[row_idx+1][col_idx] = matrix[row_idx+1][col_idx], matrix[row_idx][col_idx]

print(max_candy)