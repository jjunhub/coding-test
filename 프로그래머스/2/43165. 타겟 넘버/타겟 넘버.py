def solution(numbers, target):
    answer = 0
    
    def fun(val, next_idx):
        nonlocal answer
	
        if next_idx == len(numbers):
            if val == target:
                answer += 1
            return
        fun(val + numbers[next_idx], next_idx+1)
        fun(val - numbers[next_idx], next_idx+1)
    
    fun(0, 0)
    
    return answer