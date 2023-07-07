import sys
input = sys.stdin.readline
N, M = map(int, input().split()) # N * N 매트릭스, M 번 입력

matrix = [ 0 ] * N
sumA = [0] * (N*N + 1)
temp = 0


for i in range(N):
    matrix[i] = list(map(int, input().split()))
    for j in range(N):
        temp = temp + matrix[i][j]
        sumA[i * N + j +1] = temp 

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = 0
    for x in range(x1, x2+1) :
        firstSum = (x - 1) * N + (y1 - 1)
        secondSum = (x - 1) * N + (y2 - 1)
        result += sumA[secondSum+1] - sumA[firstSum]

    print(result)