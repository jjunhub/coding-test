def solution(brown, yellow):
    answer = []
    totalCarpet = brown + yellow
    divisorList = getDivisor(totalCarpet)
    
    for garo, sero in divisorList:
        if 2*(garo+sero) - 4 == brown:
            return [garo, sero]
    

def getDivisor(number):
    divisorList = [] # ( num1, num2 ) tuple list, num1 * num2 == number
    for num in range(3, int(number**0.5) + 1):
        if number % num == 0:
            divisorList.append((number//num, num))
    return divisorList