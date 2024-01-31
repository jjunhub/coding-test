def solution(answers):
    answer = []
    
    supo1 = [1,2,3,4,5] * (len(answers) // 5 + 1)
    supo2 = [2,1,2,3,2,4,2,5] * (len(answers)// 8 + 1) 
    supo3 = [3,3,1,1,2,2,4,4,5,5] * (len(answers)// 10 + 1)
    
    threesupo = [ supo1, supo2, supo3]
    score = [ 0, 0, 0]
    
    for idx,ans in enumerate(answers):
        for who, supo in enumerate(threesupo):
            if supo[idx] == ans:
                score[who] += 1
    
    bestPeopleCount = score.count(max(score)) 
    if bestPeopleCount == 1:
        answer.append(score.index(max(score)) + 1)
    elif bestPeopleCount == 2:
        minScorePeople = score.index(min(score)) + 1
        answer.extend([1,2,3])
        answer.remove(minScorePeople)
    else : # Same 3 score.
        answer.extend([1,2,3])
    
    return answer