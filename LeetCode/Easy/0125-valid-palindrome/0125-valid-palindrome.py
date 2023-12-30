class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStrs = []
        for char in s :
            if char.isalnum():
                newStrs.append(char.lower())
        
        return newStrs == newStrs[::-1]
        