import sys
input = sys.stdin.readline

N, K, P = map(int, (input().split()))
breads = input().split()
breads.reverse()
flag = fail = answ = 0
while breads:
  flag += 1
  val = breads.pop()
  if val == '0' :
    fail += 1
  
  if flag == K:
    if fail < P:
      answ += 1
    
    flag = 0
    fail = 0
print(answ)