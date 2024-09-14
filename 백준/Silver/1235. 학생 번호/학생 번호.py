import sys
input = sys.stdin.readline
N = int(input())
numbers = []
for _ in range(N):
  number = input().rstrip()
  numbers.append(number[::-1])

numberLen = len(numbers[0])
for jaritsu in range(1, numberLen+1):
  numberSet = set()
  for number in numbers:
    new_number = number[:jaritsu]
    if new_number in numberSet:
      break
    else :
      numberSet.add(new_number)
  if len(numberSet) == N:
    break
print(jaritsu)