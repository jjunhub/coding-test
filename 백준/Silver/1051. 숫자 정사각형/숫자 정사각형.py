def find_max_square():
  length = min(N, M)-1
  while length > 0:
    for row_idx in range(N):
      for col_idx in range(M):
        if row_idx + length < N and col_idx + length < M :
          a = matrix[row_idx][col_idx]
          b = matrix[row_idx + length][col_idx]
          c = matrix[row_idx][col_idx + length]
          d = matrix[row_idx + length][col_idx + length]
          
          if a == b == c == d :
            return length
    length -= 1
  return length

N, M = map(int, input().split())
matrix = list()
for _ in range(N):
  matrix.append(list(input()))
print((find_max_square()+1) ** 2)