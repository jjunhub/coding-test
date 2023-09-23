class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        for i in range( int(len(strX) / 2)):
            if (strX[i] != strX[len(strX) -1 - i ]):
                return False
            
        return True
            
        