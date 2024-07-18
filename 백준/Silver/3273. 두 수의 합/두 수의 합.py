import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
target = int(input())
dic = dict()
answer = 0

for num in numbers:
  dic[num] = True

for num in numbers:
  if (target-num) in dic:
    answer += 1

print(answer//2)