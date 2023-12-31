class Solution:
    def longestPalindrome(self, s: str) -> int:
        wordDict = collections.defaultdict(int)
        for letter in s:
            wordDict[letter] += 1
            
        evenVal = 0
        oddVal = 0
        biggestOddVal = 1
        oddFlag = False
        
        print(wordDict.items())
        
        for key,val in wordDict.items():
            if val % 2 == 0:
                evenVal += val
            else:
                oddFlag = True
                if val >= biggestOddVal :
                    oddVal += biggestOddVal - 1
                    biggestOddVal = val
                else :
                    oddVal += val - 1
        
        if oddFlag :
            return evenVal + oddVal + biggestOddVal
        else :
            return evenVal
                
            
            