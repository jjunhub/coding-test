answer = dict()
answer["0"] = 0
answer["-1"] = 0
answer["1"] = 0

def daq(X,Y,N):
  if is_same_number(X,Y,N):
    answer[matrix[Y][X]] += 1
    return
  
  daq(X, Y, N//3)
  daq(X + N//3, Y, N//3)
  daq(X + N//3 + N//3, Y, N//3)

  daq(X, Y + N//3, N//3)
  daq(X + N//3, Y + N//3, N//3)
  daq(X + N//3 + N//3, Y + N//3, N//3)

  daq(X, Y + N//3 + N//3, N//3)
  daq(X + N//3, Y + N//3 + N//3, N//3)
  daq(X + N//3 + N//3, Y + N//3 + N//3, N//3)

def is_same_number(X,Y,N):
  first = matrix[Y][X]
  for y in range(Y, Y+N):
    for x in range(X, X+N):
      if matrix[y][x] != first:
        return False
  return True

N = int(input())
matrix = [ input().split() for _ in range(N)]
daq(0, 0, N)

print(answer["-1"])
print(answer["0"])
print(answer["1"])