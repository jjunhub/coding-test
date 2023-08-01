# 코드
```python
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
      answer = [0] * len(temperatures)
      stack = []
      for index, temperature in enumerate(temperatures):
        while( stack and stack[-1][1] < temperature) :
            popindex, poptemp = stack.pop()
            answer[popindex] = index - popindex
        stack.append( (index, temperature) )
      return answer
```

## point1.
  stack[-1]로 top 부분을 확인하기

## point2.
  and 연산을 이용해 비어있지 않은 stack에 대해서만 pop하도록 코드를 작성
