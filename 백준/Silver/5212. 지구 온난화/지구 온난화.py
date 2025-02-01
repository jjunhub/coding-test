R, C = map(int, input().split())
matrix = [ input() for _ in range(R)]
answer = matrix[:]
min_col = 11
max_col = -1
min_row = 11
max_row = -1

for row in range(R):
  for col in range(C):
    if matrix[row][col] == "X":
      seaCount = 0
      # 상
      if row - 1 < 0 or matrix[row-1][col] == ".":
        seaCount += 1
      # 하
      if row + 1 >= R or matrix[row+1][col] == ".":
        seaCount += 1
      # 좌
      if col - 1 < 0 or matrix[row][col-1] == ".":
        seaCount += 1
      # 우
      if col + 1 >= C or matrix[row][col+1] == ".":
        seaCount += 1

      if seaCount < 3:
        min_row = min(min_row, row)
        max_row = max(max_row, row)
        min_col = min(min_col, col)
        max_col = max(max_col, col)
      else :
        answer[row] = answer[row][:col] + "." + answer[row][col+1:]
for row in range(min_row, max_row+1):
  for col in range(min_col, max_col+1):
    print(answer[row][col], end="")
  print()