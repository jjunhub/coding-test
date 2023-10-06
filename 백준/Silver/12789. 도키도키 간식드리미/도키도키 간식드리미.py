import sys
input = sys.stdin.readline

N = int(input())
studentLine = list(map(int, input().split()))
studentStack = []
correctSequence = 1

while(studentLine):
  studentNumber = studentLine.pop(0)
  if studentNumber == correctSequence:
    correctSequence += 1
    while studentStack and studentStack[-1] == correctSequence:
      studentStack.pop()
      correctSequence += 1
  else :
    studentStack.append(studentNumber)

while(studentStack):
  if studentStack[-1] == correctSequence:
    studentStack.pop()
    correctSequence += 1
  else :
    break

if not studentStack: 
  print("Nice")
else :
  print("Sad")