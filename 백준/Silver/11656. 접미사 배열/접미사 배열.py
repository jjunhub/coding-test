word = input()
smallword = []
for i in range(len(word)):
    smallword.append(word[-i:])

smallword.sort()
for str in smallword:
    print(str)