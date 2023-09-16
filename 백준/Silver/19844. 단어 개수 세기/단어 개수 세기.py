import sys
input = sys.stdin.readline

문장 = input().rstrip()
문장 = 문장.replace('-',' ')
문장 = 문장.split()
체크할단어 = ["c'", "j'", "n'", "m'", "t'", "s'", "l'", "l'", "d'", "qu'", "s'"]
모음 = ['a', 'e', 'i', 'o', 'u', 'h']
스택 = []

count = 0
for 단어 in 문장:
    if "'" in 단어:
        if 단어[:2] in 체크할단어:
            if 단어[2] in 모음 :
                count +=1
        elif 단어[:3] == "qu'":
            if 단어[3] in 모음 :
                count +=1 

print(len(문장) + count)