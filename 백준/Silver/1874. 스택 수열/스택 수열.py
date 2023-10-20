import sys
input = sys.stdin.readline

n = int(input())
target = [ int(input()) for i in range(n)]
index = 0
stack = []
stackNumber = 1
answer = []

while(index < n and stackNumber <= n):
  if stack and stack[-1] == target[index]:
    stack.pop()
    index += 1
    answer.append('-')
  else :
    stack.append(stackNumber)
    answer.append('+')
    stackNumber +=1

while stack :
  if stack[-1] == target[index]:
    stack.pop()
    index+=1
    answer.append('-')
  else :
    answer = []
    break

if answer:
  for ans in answer:
    print(ans)
else :
  print('NO')
