import collections
def solution(participant, completion):
    
    answer = ''
    participants = collections.defaultdict(int)
    
    for one in participant:
        participants[one] += 1

    for one in completion:
        participants[one] -= 1
    
    
    for key,val in participants.items():
        if val != 0:
            answer = key
            break
        
    return answer