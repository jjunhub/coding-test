from collections import deque
APPLE, NOTHING = 1, 0
LEFT, RIGHT, UP, DOWN = (0, -1), (0, 1), (-1, 0), (1, 0)

N = int(input()) 
matrix = [[ NOTHING for _ in range(N)] for _ in range(N)]

# Apple
for _ in range(int(input())):
  row, col = map(int, input().split())
  matrix[row-1][col-1] = APPLE

# Move
move_plan = []
for _ in range(int(input())):
  time, dir = input().split()
  move_plan.append((int(time), dir))
move_plan.reverse()

now_dir = RIGHT
snake = deque([(0, 0)])
time_count = 0
while True:
  time_count += 1

  snake_head_row, snake_head_col = snake[-1]
  next_snake_head_row = snake_head_row + now_dir[0]
  next_snake_head_col = snake_head_col + now_dir[1]

  # Wall
  if not (0<= next_snake_head_row< N and 0 <= next_snake_head_col < N):
     break
  
  # Crash Myself
  if (next_snake_head_row, next_snake_head_col) in snake:
    break

  snake_tail = snake.popleft()
  snake.append((next_snake_head_row, next_snake_head_col))
  
  # Apple
  if matrix[next_snake_head_row][next_snake_head_col] == APPLE:
    matrix[next_snake_head_row][next_snake_head_col] = NOTHING
    snake.appendleft(snake_tail)
  
  # Direction Change
  if move_plan and move_plan[-1][0] == time_count:
    _, dir = move_plan.pop()
    if dir == "L":
      if now_dir == RIGHT: now_dir = UP
      elif now_dir == UP: now_dir = LEFT
      elif now_dir == LEFT: now_dir = DOWN
      elif now_dir == DOWN: now_dir = RIGHT
    else : # dir == "D"
      if now_dir == RIGHT: now_dir = DOWN
      elif now_dir == DOWN: now_dir = LEFT
      elif now_dir == LEFT: now_dir = UP
      elif now_dir == UP: now_dir = RIGHT
  
print(time_count)