import sys

input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

sum = [0] # 리스트 방식으로 선언
temp = 0

for i in numbers:
    temp = temp + i
    sum.append(temp)    

for _ in range(M) :
    i, j = map(int, input().split())
    print(sum[j]-sum[i-1])