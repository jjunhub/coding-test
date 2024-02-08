from itertools import permutations
def solution(k, dungeons):
    answer = -1
    for dungeonsNum in range(1, len(dungeons)+1):
        for dungeonInfos in permutations(dungeons, dungeonsNum):
            hp = k
            count = 0
            for minPiro, needPiro in dungeonInfos:
                
                if hp >= minPiro and hp >= needPiro : # 탐험 진행
                    hp -= needPiro
                    count += 1
                else : # 탐험 중지
                    break
            answer = max(count, answer)
            
    return answer