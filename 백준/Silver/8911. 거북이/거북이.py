import sys
from collections import deque
input = sys.stdin.readline

NORTH = (0, 1)
EAST = (1, 0)
SOUTH = (0, -1)
WEST = (-1, 0)
START_POINT = (0, 0)
RESET = [NORTH, EAST, SOUTH, WEST]

testcase = int(input())
for _ in range(testcase):
  command = input().rstrip()
  point = START_POINT
  direction = deque(RESET[:])
  max_x, min_x, max_y, min_y = 0, 0, 0, 0

  for move in command:
    heading = direction[0]
    if move == "F":
      point = (point[0] + heading[0], point[1] + heading[1])
    elif move == "B":
      point = (point[0] - heading[0], point[1] - heading[1])
    elif move == "L":
      direction.rotate(1)
    elif move == "R":
      direction.rotate(-1)

    max_x = max(max_x, point[0])
    min_x = min(min_x, point[0])
    max_y = max(max_y, point[1])
    min_y = min(min_y, point[1])

  print((max_x-min_x) * (max_y-min_y))
