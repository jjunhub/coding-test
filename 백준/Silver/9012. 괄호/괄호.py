import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    stack = []
    flag = 0 # default 
    testcase = input().strip()
    
    for i in testcase:
        if i == "(" : stack.append(i)
        else :  # )
          if len(stack) == 0 : 
             flag = 1 # fail
             break
          stack.pop()

    # fail or stack remain anything
    if(flag == 1 or len(stack) != 0): print("NO")
    else : print("YES")