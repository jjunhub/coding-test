import sys

input = sys.stdin.readline

N = int(input()) # 배열의 개수
numbers = list(map(int, input().split()))
M = int(input()) # 구간합을 구할 횟수

sumOfNumbers = [0]
temp = 0
for num in numbers:
    temp += num
    sumOfNumbers.append(temp)

for _ in range(M):
    left, right = map(int, input().split())
    print(sumOfNumbers[right] - sumOfNumbers[left-1])
