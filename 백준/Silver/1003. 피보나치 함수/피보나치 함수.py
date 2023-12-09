import sys
input = sys.stdin.readline

T = int(input())

fibo = [ (1,0), (0,1)]
for i in range(2, 41):
  fibo.append( (fibo[i-1][0] + fibo[i-2][0], fibo[i-1][1] + fibo[i-2][1]) )

for _ in range(T) :
  N = int(input())
  print(*fibo[N])
  