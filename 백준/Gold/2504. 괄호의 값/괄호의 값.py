OPEN_SMALL, CLOSE_SMALL = "(", ")"
OPEN_BIG, CLOSE_BIG = "[", "]"

def getSetOfGalho(galho):
  if galho == OPEN_SMALL:
    return CLOSE_SMALL

  if galho == CLOSE_SMALL:
    return OPEN_SMALL
  
  if galho == OPEN_BIG:
    return CLOSE_BIG
  
  if galho == CLOSE_BIG:
    return OPEN_BIG

def galhoToScore(galho):
  if galho in [OPEN_SMALL , CLOSE_SMALL]:
    return 2
  else:
    return 3
  
def isNumber(galho):
  if galho in [OPEN_BIG, OPEN_SMALL, CLOSE_BIG, CLOSE_SMALL]:
    return False
  
  return True

galhos = input()
stack = []
answer = 0
flag = True

for galho in galhos:
  if galho == OPEN_SMALL or galho == OPEN_BIG:
    stack.append(galho)
  
  else: # 닫는게 들어오는 경우
    temp = 0
    if not stack:
      flag = False
    while True and flag:
      if stack and stack[-1] == getSetOfGalho(galho):
        stack.pop() # 스택에 있던 여는 괄호 빼기
        score = galhoToScore(galho)
        totalScore = score if temp==0 else temp*score
        stack.append(totalScore) # 점수 쌓아두기
        break
      elif stack and isNumber(stack[-1]): 
        if len(stack) > 1:
          temp += stack.pop()
        else:
          break
      elif stack and stack[-1] != getSetOfGalho(galho):
        flag = False
        break
      else:
        break
    
    if flag == True and len(stack) == 1:
      answer += stack.pop()

if flag == True:
  print(answer)
else:
  print(0)