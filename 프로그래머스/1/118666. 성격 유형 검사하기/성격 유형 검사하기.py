from collections import defaultdict
# 0. 각 성격 점수를 저장할 수 있는 Dictionary 선언
# 1. survey와 choices를 zip으로 묶어서, loop마다 성격 점수 체크
# 2. 점수를 바탕으로 최종 성격 유형을 결정
personality_list = ("RT", "CF", "JM", "AN")

def solution(survey, choices):
    personality_score = apply_survey_result(survey, choices)
    answer = ''
    
    for i in personality_list:
        if personality_score[i[0]] + 0.1 > personality_score[i[1]]:
            answer += i[0]
        else :
            answer += i[1]    
    
    return answer

def apply_survey_result(survey:list, choices:list) -> dict:
    personality_score = defaultdict(int)
    for personalities, choice in zip(survey, choices):
        if choice < 4 :
            # 앞의 성격으로
            personality = personalities[0]
            personality_score[personality] += abs(choice-4)
        elif choice > 4:
            # 뒤의 성격으로
            personality = personalities[1]
            personality_score[personality] += abs(choice-4)
            
    return personality_score