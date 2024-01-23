import sys
input = sys.stdin.readline

N = int(input())
tops = list(map(int, input().split())) # N5
stack = []
result = []
idx = 0

while tops : # Total 2N
  # print(f'tops = {tops}, stack = {stack}, result = {result}')
  top = tops.pop()
  receiveTopNum = 0

  if not stack :
    stack.append((N - idx - 1, top))
  else :  
    if stack[-1][1] < top:
      while stack and stack[-1][1] < top: # Total N
        result.append( (stack.pop()[0], N - idx) )
      stack.append((N - idx - 1, top))
    else :
      stack.append((N - idx - 1, top))
  idx += 1

answer = [0] * N
for idx, val in result:
  answer[idx] = val

print(*answer)