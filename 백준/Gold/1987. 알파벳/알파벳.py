from collections import deque

def bfs(s_row : int, s_col : int, rows :int, cols :int) -> int:
  DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  max_distance = 0
  q = deque()
  visited = set()
  alphabets = 1 << (ord(matrix[s_row][s_col]) - 65)
  q.append((s_row, s_col, alphabets, 1))
  visited.add((s_row, s_col, alphabets))
  
  while q:
    cur_row, cur_col, visited_alphabets, alphabets_count = q.popleft()
    max_distance = max(max_distance, alphabets_count)
  
    for dr, dc in DIRECTIONS:
      next_row, next_col = cur_row + dr, cur_col + dc
      
      if not ( 0 <= next_row < rows and 0 <= next_col < cols):
        continue

      next_alphabet = matrix[next_row][next_col]
      if visited_alphabets & ( 1 << (ord(next_alphabet)- 65)) == False:
        new_visited_alphabets = visited_alphabets | ( 1 << (ord(next_alphabet)- 65))
        if (next_row, next_col, new_visited_alphabets) in visited:
          continue
        visited.add((next_row, next_col, new_visited_alphabets))
        q.append((next_row, next_col, new_visited_alphabets, alphabets_count+1))
      
  return max_distance

R, C = map(int, input().split())
matrix = [list(input()) for _ in range(R)]
print(bfs(0,0,R,C))