def solution(numbers):
    answer = ''
    changeNum = []
    for idx, num in enumerate(numbers):
        if num < 10: # 2 -> 222
            num = str(num) * 4
        elif num < 100: # 26 -> 2626
            num = (str(num) * 2)
        elif num < 1000: # 263 -> 2632
            num = (str(num) * 2)[:4]
        
        changeNum.append((idx, int(num)))
    
    changeNum.sort(key = lambda x : x[1], reverse = True)
    
    for idx, _ in changeNum:
        answer += str(numbers[idx])
    
    if answer[0] == "0":
        return "0"
    else :
        return answer