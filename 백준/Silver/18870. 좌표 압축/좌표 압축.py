import sys
input = sys.stdin.readline

N = int(input())
Numbers = list(map(int, input().split()))
CompressedNumbers = {}

Numbers_NotDup = list(set(Numbers))
Numbers_NotDup.sort()

for index, number in enumerate(Numbers_NotDup):
  CompressedNumbers[number] = index

for number in Numbers:
  print(CompressedNumbers[number], end = " ")