def solution(progresses, speeds):
    answer = []
    days = []
    for p, s in zip(progresses, speeds):
        days.append( -(-(100-p)//s))

    print(days)
    doneDay = days[0]
    temp = 1
    
    for idx in range(1, len(days)):
        if days[idx] <= doneDay:
            temp += 1
        else :
            answer.append(temp)
            doneDay = days[idx]
            temp = 1
            
    answer.append(temp)
    return answer