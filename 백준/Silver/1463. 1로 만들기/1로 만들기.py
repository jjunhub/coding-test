import sys
input = sys.stdin.readline

N = int(input())

D = [0] * 1000001
D[1] = 0

for i in range(2, N+1):
    D[i] = D[i-1] + 1
    if i % 2 == 0 : 
        D[i] = D[i//2] + 1 if D[i//2] < D[i] else D[i]
    if i % 3 == 0 :
        D[i] = D[i//3] + 1 if D[i//3] < D[i] else D[i] 
    # print(f'D[{i}] = {D[i]}')
print(D[N])