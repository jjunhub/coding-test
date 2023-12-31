class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestWord = []
        for mid in range(len(s)):
            for case in range(2):
                # when case = 0, start with one char. ex) a -> bab -> ...
                # when case = 1, start with two char. ex) bb -> abba -> ...
                left = mid
                right = mid + case
                while left >= 0 and right <= len(s)-1 and s[left] == s[right]:
                    left -= 1
                    right += 1
                word = s[left+1 : right]            
                longestWord = max(word, longestWord, key= len)
                    
        return longestWord
                
            
        
            
        
            
            
            