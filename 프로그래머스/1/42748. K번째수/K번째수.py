def solution(array, commands):
    answer = []
    for idx in range(len(commands)):
        i, j, k = commands[idx]
        b = sorted(array[i-1:j])
        answer.append(b[k-1])
        
    return answer