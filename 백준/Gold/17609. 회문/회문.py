import sys
import copy
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  word = input().rstrip()
  caseFlag = 0
  leftPtr = 0
  rightPtr = len(word) - 1
  while(leftPtr < rightPtr):
    if word[leftPtr] == word[rightPtr]:
      leftPtr += 1
      rightPtr -= 1 
    elif rightPtr - leftPtr == 1 :
      caseFlag = 1
      leftPtr += 1
      rightPtr -= 1 
    else :
      if word[leftPtr+1] == word[rightPtr] or word[leftPtr] == word[rightPtr-1]:
        caseFlagA = 2
        caseFlagB = 2
        templeftPtr = leftPtr
        temprightPtr = rightPtr

        if word[leftPtr+1] == word[rightPtr] :
          leftPtr += 1
          while(leftPtr < rightPtr):
            if word[leftPtr] == word[rightPtr]:
              leftPtr += 1
              rightPtr -= 1
            else :
              caseFlagA = 2
              break
            caseFlagA = 1
        
        if word[templeftPtr] == word[temprightPtr-1] :
          temprightPtr -= 1
          while(templeftPtr < temprightPtr):
            if word[templeftPtr] == word[temprightPtr]:
              templeftPtr += 1
              temprightPtr -= 1
            else :
              caseFlagB = 2
              break
            caseFlagB = 1

        caseFlag = min(caseFlagA, caseFlagB)
        break
      else:
        caseFlag = 2
        break
      
  print(caseFlag)