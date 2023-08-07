import sys
input = sys.stdin.readline

infix = input().rstrip()
priority = {
    "(" : -1, # for non-char check
    ")" : -1, # for non-char check
    "*" : 1,
    "/" : 1,
    "+" : 0,
    "-" : 0,
}

result = []
operatorStack = []

for char in infix :
    charAttr = priority.get(char, 'word')
    if charAttr == 'word' :
        result.append(char)
    else :
        if len(operatorStack) == 0 or char == "(": # 아무것도 없을 때 또는 여는 괄호일 때
            operatorStack.append(char)
        elif priority.get(operatorStack[-1]) < priority.get(char) : # top이 새로운 것보다 우선 순위가 더 작을 때 넣기
            operatorStack.append(char)
        elif char == ")" :
            while(len(operatorStack)!= 0):
                tempPop = operatorStack.pop()
                if tempPop == "(" : 
                    break
                result.append(tempPop)
        else : # top이 새로운 것보다 우선 순위가 클 때, pop한다. 이 과정을 top의 우선 순위가 새로운 것보다 더 작을때까지
            while(len(operatorStack) != 0):
                if (priority.get(operatorStack[-1]) >= priority.get(char)):
                    result.append(operatorStack.pop())
                else :
                    break
            operatorStack.append(char)
            
while(len(operatorStack)!=0) :
    result.append(operatorStack.pop())

print("".join(result))