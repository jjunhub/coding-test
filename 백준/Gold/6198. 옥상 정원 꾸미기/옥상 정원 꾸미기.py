import sys
input = sys.stdin.readline
MAX_HEIGHT = 1000000000

nubmer_of_building = int(input())
building_stack = []
count = 0

for building_number in range(1, nubmer_of_building+2):
  if building_number == nubmer_of_building+1:
    height = MAX_HEIGHT
  else :
    height = int(input())

  while building_stack and building_stack[-1][1] <= height: # top과 비교
    count += (building_number - 1) - building_stack[-1][0]
    building_stack.pop()
    
  building_stack.append((building_number, height))

print(count)