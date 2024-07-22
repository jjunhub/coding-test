import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
  queue = deque()
  for fire_pos_h, fire_pos_y in fire_pos_li:
    queue.append((fire_pos_h, fire_pos_y, 0, "F"))
  queue.append((start[0], start[1], 0, "J")) # (위치, 시간)

  dir = [(1, 0), (-1, 0), (0, -1), (0, 1)] # 상, 하, 좌, 우

  while queue:
    el_hang, el_yeol, time, type = queue.popleft()
    
    for idx in range(4):
      next_hang = el_hang + dir[idx][0]
      next_yeol = el_yeol + dir[idx][1]

      # 바깥인지 체크
      if (not 0 <= next_hang < hang) or (not 0 <= next_yeol < yeol):
        if type == "J" :
          return time+1
        else :
          continue
      
      # 벽, 불인지 체크
      if matrix[next_hang][next_yeol] == "#" or matrix[next_hang][next_yeol] == "F":
        continue

      # type에 따라 확산
      if type == "F":
        if matrix[next_hang][next_yeol] == "J" or matrix[next_hang][next_yeol] == ".":
          matrix[next_hang][next_yeol] = "F"
          queue.append((next_hang, next_yeol, time+1, type))
        
      elif type == "J":
        if matrix[next_hang][next_yeol] == ".":
          matrix[next_hang][next_yeol] = "J"
          queue.append((next_hang, next_yeol, time+1, type))

  return "IMPOSSIBLE"

hang, yeol = map(int, input().split())
jihoon_pos = 0
fire_pos_li = []
matrix = []

for h in range(hang):
  line = input().rstrip()
  temp_yeol = []
  for y, el in enumerate(line):
    if el == "J" :
      jihoon_pos = (h, y)
    elif el == "F":
      fire_pos_li.append((h,y))

    temp_yeol.append(el)
  matrix.append(temp_yeol)

print(bfs(jihoon_pos))