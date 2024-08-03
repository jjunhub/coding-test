import sys
from collections import deque
input = sys.stdin.readline

def one_year_later() -> set:
  have_to_go = set()
  for h in range(hang):
    for y in range(yeol):
      if matrix[h][y] > 0:
        have_to_go.add((h,y))
  return have_to_go
      
def bfs(start : tuple, visited_matrix : set, melted_place : set):
  h, y = start
  visited_matrix.add((h,y))
  q = deque()
  q.append((h,y))
  dir = [(1,0), (-1,0), (0,-1), (0,1)] # 상하좌우

  while q:
    h, y = q.popleft()
    melted_amount = 0

    for i in range(4):
      next_h, next_y = h + dir[i][0], y + dir[i][1]

      if not ( 0 <= next_h < hang and 0 <= next_y < yeol):
        continue
      
      if (next_h, next_y) not in visited_matrix and matrix[next_h][next_y] > 0:
        visited_matrix.add((next_h, next_y))
        q.append((next_h, next_y))
      
      if matrix[next_h][next_y] == 0:
        melted_amount += 1
    
    melted_place.add((h, y, melted_amount))

def find_ice_berg() -> int:
  year = 0

  while True:
    have_to_go = one_year_later()
    if 0 <= len(have_to_go) <= 1:
      return 0
    
    visited_matrix = set()
    melted_place = set()
    ice_berg_number = 0

    for h, y in have_to_go:
      if (h,y) not in visited_matrix:
        bfs((h,y), visited_matrix, melted_place)
        ice_berg_number += 1
    
    for h,y,melted_amount in melted_place:
      matrix[h][y] = max( matrix[h][y]-melted_amount, 0)

    if ice_berg_number > 1 :
      return year
    
    year += 1

hang, yeol = map(int, input().split())
matrix = []
for _ in range(hang):
  matrix.append(list(map(int, input().split())))

print(find_ice_berg())