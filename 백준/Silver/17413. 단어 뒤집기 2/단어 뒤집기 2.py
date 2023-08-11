import sys
input = sys.stdin.readline

S = input().rstrip()
index = 0
tempStr = ""
resultStr = ""

def reverseStr(string):
   temp = list(string)
   temp.reverse()
   return ''.join(char for char in temp)

while(True):
    if S[index] == "<":
      resultStr += reverseStr(tempStr)
      tempStr = ""
      while(S[index] != ">"):
         tempStr += S[index]
         index += 1
      tempStr += ">"
      resultStr += tempStr
      tempStr = ""
      index += 1 
    elif S[index] == " ":
      resultStr += reverseStr(tempStr) + " "
      tempStr = ""
      index += 1
    else :
      tempStr += S[index]
      index += 1

    if(index == len(S)) :
       tempStr = reverseStr(tempStr)
       resultStr += tempStr
       break

print(resultStr)