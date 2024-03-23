import sys

bingo = [ list(map(int,input().split())) for _ in range(5) ]
answer = [ list(map(int,input().split())) for _ in range(5) ]
checked = [ [ False] * 5 for _ in range(5) ]
result = -1

def markbingo(num):
  for y in range(5):
    for x in range(5):
      if bingo[y][x] == num:
        checked[y][x] = True
        return
      
def checkbingo():
  bingoCount = 0

  # check garo
  for y in range(5):
    count = 0
    for x in range(5):
      if checked[y][x]:
        count += 1
    if count == 5:
      bingoCount += 1

  # check sero
  for y in range(5):
    count = 0
    for x in range(5):
      if checked[x][y]:
        count += 1
    if count == 5:
      bingoCount += 1

  # check daegak
  count = 0
  for x in range(5):
    if checked[x][x]:
      count += 1
    
  if count == 5:
    bingoCount += 1

  # check daegak
  count = 0
  for x in range(5):
    if checked[4-x][x]:
      count +=1 
      
  if count == 5:
    bingoCount += 1
  
  return bingoCount

      
for y in range(5):
  for x in range(5):
    if result > 0:
      continue
    num = answer[y][x]
    markbingo(num)
    if checkbingo() >= 3:
      result = (y) * 5 + ( x + 1)

print(result)