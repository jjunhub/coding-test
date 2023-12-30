class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        for log in logs:
            identifier = log.split()[1]
            if identifier.isdigit():
                digits.append(log)
            else :
                letters.append(log)
        result = sorted(letters, key = lambda x : (x.split()[1:], x.split()[0]))
        return result + digits
