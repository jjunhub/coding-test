import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Board = [ input().rstrip() for _ in range(N)]

# chessBoard starting point (n, m)
min = 64
for n in range(0, N-7):
  for m in range(0, M-7):
    # check 8 * 8 with white start
    temp = 0
    for j in range(8):
      for i in range(0,7,2):
        if j % 2 == 0: 
          if Board[n+j][m+i] == "B":
            temp +=1
          if Board[n+j][m+i+1] == "W":
            temp +=1 
        else :
          if Board[n+j][m+i] == "W":
            temp += 1
          if Board[n+j][m+i+1] == "B":
            temp += 1
    if temp < min :
      min = temp
    
    # check 8 * 8 with black start
    temp = 0
    for j in range(8):
      for i in range(0,7,2):
        if j % 2 == 0: 
          if Board[n+j][m+i] == "W":
            temp +=1
          if Board[n+j][m+i+1] == "B":
            temp +=1 
        else :
          if Board[n+j][m+i] == "B":
            temp += 1
          if Board[n+j][m+i+1] == "W":
            temp += 1
    if temp < min :
      min = temp
print(min)