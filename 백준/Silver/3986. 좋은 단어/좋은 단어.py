import sys
input = sys.stdin.readline

def checker(word):
    if len(word) % 2 != 0 : 
       return False
    
    wordStack = []
    beforeChar = None

    for char in word:
        if beforeChar == char :
            wordStack.pop()
            beforeChar = None if not wordStack else wordStack[-1]
        else :
            wordStack.append(char)
            beforeChar = char
    
    return not len(wordStack)


N = int(input())
goodWordCount = 0

for _ in range(N):
    word = input().rstrip()
    if checker(word) :
        goodWordCount +=1 

print(goodWordCount)