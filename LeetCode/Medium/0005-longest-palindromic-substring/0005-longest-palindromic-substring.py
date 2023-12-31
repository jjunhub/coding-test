class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longestWord = s[0]
        wordLen = 2
        
        while wordLen <= len(s):
            print(wordLen)
            for leftPtr in range( len(s) - wordLen + 1):
                startleftPtr = leftPtr
                rightPtr = leftPtr + wordLen - 1
                
                
                while leftPtr <= rightPtr and s[leftPtr] == s[rightPtr]:
                    leftPtr += 1
                    rightPtr -= 1
                    
                if leftPtr > rightPtr:
                    longestWord = s[startleftPtr: startleftPtr+wordLen]
                    print(longestWord)
                    break
                    
            
            wordLen += 1
            
        return longestWord
                    
            
            
        
            
            
            