def solution(arr):
    answer = []
    answer.append(arr.pop())
    while arr:
        if arr[-1] == answer[-1]:
            arr.pop()
        else :
            answer.append(arr.pop())
    
    answer.reverse()
    return answer