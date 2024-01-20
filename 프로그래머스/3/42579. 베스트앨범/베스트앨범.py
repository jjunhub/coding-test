import collections
def getTwoBig(oneGenreList, newSongPlayTime, idx):
    if len(oneGenreList) < 3 :
        oneGenreList.append((newSongPlayTime, idx))
    else :
        smallIdx = 1
        smallPlays = oneGenreList[1][0] 
        if oneGenreList[2][0] < smallPlays:
            smallIdx = 2
            smallPlays = oneGenreList[2][0]
            
        if smallPlays < newSongPlayTime:
            oneGenreList[smallIdx] = (newSongPlayTime, idx)
        
    
def solution(genres, plays):
    answer = []
    _dict = collections.defaultdict(list)
    
    for idx in range(len(genres)):
        genre = genres[idx]
        playTime = plays[idx]
        
        if len(_dict[genre]) == 0:
            _dict[genre] = [playTime] # total music PlayTime
            _dict[genre].append((playTime, idx))
        else :
            _dict[genre][0] += playTime
            getTwoBig(_dict[genre], playTime, idx)
            
    sortedDict = sorted(_dict.values(), key = lambda x : x[0], reverse=True)
    
    for oneGenre in sortedDict:  
        sortedOneGenre = sorted(oneGenre[1:], key = lambda x : (x[0], -x[1]), reverse = True)
    
        for playNum, idx in sortedOneGenre:
            answer.append(idx)
            
    return answer