import sys
input = sys.stdin.readline

T = int(input())
D = [0] * 12 # input < 11, but we start at 1
D[1] = 1
D[2] = 2
D[3] = 4
for i in range(4, 11):
    D[i] = D[i-1] + D[i-2] + D[i-3]

for i in range(T):
    n = int(input())
    print(D[n])
