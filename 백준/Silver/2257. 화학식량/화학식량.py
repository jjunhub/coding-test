import sys
input = sys.stdin.readline

HCO = input().rstrip()

result = 0
stack = []
elements = {
    "H" : 1,
    "C" : 12,
    "O" : 16,
    "(" : -1
}
numbers = [str(i) for i in range(10)]

for one in HCO :
    if one in elements: # H, C, O, (
        stack.append(one)
    elif one in numbers :
        popValue = stack.pop()
        tempResult = 0
        if popValue in elements:
            tempResult += elements[popValue]
        else :
            tempResult += popValue
        stack.append(tempResult * int(one))
    else : # ) 
        tempResult = 0
        while True :
            popValue = stack.pop()
            if popValue == "(":
                stack.append(tempResult)
                break
            elif popValue in elements:
                tempResult += elements[popValue]
            else :
                tempResult += popValue

while stack:
    popValue = stack.pop()
    if popValue in elements:
        result += elements[popValue]
    else :
        result += popValue

print(result)