class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longestWord = []
        for mid in range(len(s)):
            left = mid
            right = mid
            while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
                left -= 1
                right += 1
            word = s[left+1 : right]            
            if len(longestWord) <= len(word):
                longestWord = word
                
            left = mid
            right = mid + 1
            while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
                left -= 1
                right += 1
            word = s[left+1 : right]            
            if len(longestWord) <= len(word):
                longestWord = word
                
        return longestWord
                
            
            
            
        
            
            
            