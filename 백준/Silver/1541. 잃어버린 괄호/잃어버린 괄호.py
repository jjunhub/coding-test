sik = input()

splitsik = []
tempWord = ""
for i in sik:
  if i == "-" or i == "+":
    splitsik.append(int(tempWord))
    splitsik.append(i)
    tempWord = ""
  else :
    tempWord += i
splitsik.append(int(tempWord))
splitsik.reverse()

result = 0
result += splitsik.pop()
tempResult = []
isMinus = False

while splitsik:
  a = splitsik.pop()
  if a == "+":
    tempResult.append(splitsik.pop())
  else : # a == "-"
    if isMinus :
      while tempResult:
        result -= tempResult.pop()
    else :
      while tempResult:
        result += tempResult.pop()
    tempResult.append(splitsik.pop())
    isMinus = True

while tempResult:
  if isMinus:
    result -= tempResult.pop()
  else :
    result += tempResult.pop()

print(result)
