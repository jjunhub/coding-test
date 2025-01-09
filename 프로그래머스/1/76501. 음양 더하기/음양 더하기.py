def solution(absolutes, signs):
    answer = 0
    for number, sign in zip(absolutes, signs):
        sign = 1 if sign else -1
        answer += number * sign
    return answer