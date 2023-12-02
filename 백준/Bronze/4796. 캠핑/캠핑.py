import sys
input = sys.stdin.readline

num = 0
while True:
  num += 1
  L, P, V = map(int, input().split())
  if L == 0 and P ==0 and V == 0:
    break

  cycle = V // P
  remain = V - cycle * P
  if remain > L :
    result = cycle * L + L
  else :
    result = cycle * L + remain
  print(f"Case {num}: {result}") 