R, C = map(int, input().split())
matrix = [ list(input()) for _ in range(R)]
answer = [ line[:] for line in matrix ]
max_col, min_col = -1, C
max_row, min_row = -1, R
mv = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for row in range(R):
  for col in range(C):
    if matrix[row][col] == 'X':
      seaCount = 0
      for dr, dc in mv:
        next_row, next_col = row + dr, col + dc

        if not ( 0 <= next_row < R and 0 <= next_col < C) or matrix[next_row][next_col] == ".":
          seaCount += 1
        
      if seaCount >= 3:
        answer[row][col] = "."
      else :
        min_row = min(min_row, row)
        max_row = max(max_row, row)
        min_col = min(min_col, col)
        max_col = max(max_col, col)

for row in range(min_row, max_row+1):
  for col in range(min_col, max_col+1):
    print(answer[row][col], end="")
  print()