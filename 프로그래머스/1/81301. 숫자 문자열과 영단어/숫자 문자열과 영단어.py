# 1. 각 영단어들을 숫자로 변경할 수 있도록, 영단어 : 숫자 형태로 딕셔너리에 저장
# 2. 문자열 s에 대해서 한 글자씩 읽어가며 영단어가 완성될 때, 이를 숫자로 바꿔서 정답지에 저장
# 2.1 한 글자가 숫자라면, pass
# 2.2 한 글자가 문자라면, 기존의 word에다가 더한 뒤에 word_to_number에서 값 있는지 확인
# 2.2.1 있으면 숫자로 변경 후, word 초기화
# 2.2.2 없으면 pass

def solution(s):
    word_to_number = {
        "zero" : '0', "one" : '1', "two" : '2', "three" : '3', "four" : '4',
        "five" : '5', "six" : '6', "seven" : '7', "eight" : '8', "nine" : '9'
    }
    answer = ""
    word = ""
    for i in s:
        if ord('a') <= ord(i) <= ord('z'):
            word += i
            if word in word_to_number:
                number = word_to_number[word]
                answer += number
                word = ""
        else :
            answer += i
    return int(answer)