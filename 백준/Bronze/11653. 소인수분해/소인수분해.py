N = int(input())

B = N
A = 2

for i in range(2, N+1):
  while B % i == 0:
    print(i)
    B = B // i
  
  if B == 1:
    break