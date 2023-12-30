class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        _dict = collections.defaultdict(int)
        paragraph = list(paragraph.lower())
        maxWordCount = -1
        maxWordKey = -1
        for idx in range(len(paragraph)):
            if paragraph[idx] in ["!", "?", "'", ",", ";", "."]:
                paragraph[idx] = " "
        newParagraph = "".join(paragraph).split()
        for word in newParagraph:
            if word not in banned:
                _dict[word] += 1
                if maxWordCount < _dict[word]:
                    maxWordCount = _dict[word]
                    maxWordKey = word
        
        return maxWordKey
    