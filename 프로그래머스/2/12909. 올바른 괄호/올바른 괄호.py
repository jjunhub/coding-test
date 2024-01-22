def solution(s):
    stack = []
    for i in s:
        if i == "(": 
            stack.append(i)
        else : # i == ")"
            if not stack or stack[-1] != "(":
                return False
            else : # stack[-1] == "("
                stack.pop()
    return not stack