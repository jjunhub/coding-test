import sys
input = sys.stdin.readline

N = int(input())
seat = input().rstrip()

i = 0
result = 1
while i < N:
  if seat[i] == 'S' :
    result += 1
    i += 1
  else :
    result += 1
    i += 2
  
if result > N:
  print(N)
else :
  print(result)