import sys
input = sys.stdin.readline

stack = []

def push(num):
    global stack
    stack.append(num)

def pop(num):
    global stack
    if(empty()):
      return -1
    else :
      return stack.pop(num)

def size():
    global stack
    return len(stack)

def empty():
    global stack
    if len(stack) == 0 :
        return 1
    else :
        return 0
    


N = int(input())
for _ in range(N):
    cmd = list(input().split())
    if cmd[0] == "push":
        push(int(cmd[1]))
    elif cmd[0] == "pop":
        print(pop(0))
    elif cmd[0] == "size":
        print(size())
    elif cmd[0] == "empty":
        print(empty())
    elif cmd[0] == "front":
        if(empty()) :
          print("-1")
        else :
          print(stack[0])
    elif cmd[0] == "back":
        if(empty()):
          print(-1)
        else :
          print(stack[len(stack)-1])
        
        
        
    
