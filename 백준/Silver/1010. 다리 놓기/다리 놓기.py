import sys, math

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    result = math.comb(b,a)
    print(result)