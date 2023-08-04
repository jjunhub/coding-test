import sys
input = sys.stdin.readline

N = int(input())
M = int(input()) # target value

ingredients = list(map(int,input().split()))
ingredients.sort()

leftPtr = 0
rightPtr = len(ingredients) - 1
armor = 0

while(leftPtr < rightPtr):
    result = ingredients[leftPtr] + ingredients[rightPtr]
    if result < M :
        leftPtr += 1
    elif result > M :
        rightPtr -= 1
    else : # result == M
        armor += 1
        leftPtr += 1

print(armor)