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