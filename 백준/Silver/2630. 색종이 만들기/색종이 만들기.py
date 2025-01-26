def dq(st_x, st_y, end_x, end_y) -> str :
  if check_same_color(st_x,st_y,end_x,end_y) :
    return str(matrix[st_x][st_y])
  
  a = (end_x - st_x)//2
  return dq(st_x, st_y, st_x+a, st_y+a) + dq(st_x+a, st_y, end_x, end_y-a) + dq(st_x, st_y+a, end_x-a, end_y) + dq(st_x+a, st_y+a, end_x, end_y)

def check_same_color(st_x, st_y, end_x, end_y):
  first = matrix[st_x][st_y]
  for y in range(st_y, end_y):
    for x in range(st_x, end_x):
      if matrix[x][y] != first:
        return False
  return True

N = int(input())
matrix = [ list(map(int, input().split())) for _ in range(N) ]
answer = dq(0,0,N,N)
print(answer.count("0"))
print(answer.count("1"))