class Solution:
    def reverseString(self, s: List[str]) -> None:
        leftPtr = 0
        rightPtr = len(s) - 1
        while (leftPtr <= rightPtr):
            s[leftPtr], s[rightPtr] = s[rightPtr], s[leftPtr] 
            leftPtr += 1
            rightPtr -= 1
        