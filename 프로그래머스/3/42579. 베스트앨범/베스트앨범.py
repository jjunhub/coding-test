import collections
def solution(genres, plays):
    answer = []
    genreDict = collections.defaultdict()
    
    for i, (genre,play) in enumerate(zip(genres, plays)):
        if genre in genreDict:
            genreDict[genre][0] += play
            genreDict[genre].append((i, play))
        else:
            genreDict[genre] = [play]
            genreDict[genre].append((i, play))
            
    sortedDict = sorted(genreDict.items(), key = lambda x:x[1], reverse=True) 
    
    for i in sortedDict:
        tempList = sorted(i[1][1:],  key = lambda x:x[1], reverse = True)
        print(tempList)
        if len(tempList) < 2 :
            answer.append(tempList[0][0])
        else :
            answer.append(tempList[0][0])
            answer.append(tempList[1][0])
            
    return answer