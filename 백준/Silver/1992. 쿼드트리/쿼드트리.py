def dac(x, y, N) -> str:
  if can_zip(x,y,N):
    return matrix[y][x]

  return "(" + dac(x, y, N//2) + dac(x + N//2, y, N//2) + dac(x, y+ N//2, N//2) + dac(x + N//2, y + N//2, N//2) + ")"

def can_zip(X,Y,N) -> bool:
  first = matrix[Y][X]
  for y in range(Y, Y+N):
    for x in range(X, X+N):
      if matrix[y][x] != first:
        return False
  return True

N = int(input())
matrix = [ list(input()) for _ in range(N) ]
print(dac(0,0,N))