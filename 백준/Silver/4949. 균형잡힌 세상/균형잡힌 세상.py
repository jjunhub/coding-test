import sys
input = sys.stdin.readline

while(True):
  line = input().rstrip()
  if( line == ".") : break

  stack = []
  flag = 1 # 1 is yes

  for char in line :
    if char not in ["(", ")", "[", "]"] :
      continue
    
    if char == "(" :
      stack.append(")")
    elif char == "[" :
      stack.append("]")
    else :
      if len(stack) == 0 or char != stack.pop():
        flag = 0
        break

  if len(stack) == 0 and flag == 1 :
    print("yes")
  else :    
    print("no")