# 문제
```python
class Solution:
    def isValid(self, s: str):
        stack = []
        for char in s :
            if char == "(": 
                stack.append(")")
            elif char == "{":
                stack.append("}")
            elif char == "[":
                stack.append("]")
            elif not stack or stack.pop() != char:
                return False
        return not stack
```

## Point1.
    빈 리스트는 False를 반환한다.
        
## Point2.
     or 연산자들 통해 not stack 조건과 stack.pop() != char 조건을 파악하였다.
     이 경우에 not stack이라는 조건, 즉 stack이 비었다는 조건이 만족되면 뒤에 있는 stack.pop() != char 조건을 따지지 않고
     False를 반환하도록 하여, 빈 리스트에 대해 pop을 진행하는 error을 막을 수 있다.
