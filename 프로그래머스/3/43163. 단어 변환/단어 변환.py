from collections import defaultdict, deque

def makeGraph(words):
    graph = defaultdict(list)
    for wordIdx, word in enumerate(words):
        # 한 단어씩, 한 글자씩 비교한다.
        for otherWord in words:
            # 같은 단어라면 패스
            if word == otherWord : pass

            count = 0
            for idx in range(len(word)):
                if word[idx] != otherWord[idx]: count += 1
                if count > 1: break

            if count == 1:
                graph[word].append(otherWord)
    return graph

def bfs(graph, words, begin, target):
    queue = deque()
    queue.append((begin, 0))
    visited = set()
    
    while queue:
        cur_v, count = queue.popleft()
        if cur_v == target :
            return count
        
        for word in graph[cur_v]:
            if word not in visited:
                visited.add(word)
                queue.append((word, count+1))
    return 0           

def solution(begin, target, words):
    answer = 0    
    if target not in words:
        return answer
    
    words.append(begin)
    graph = makeGraph(words)
    answer = bfs(graph, words, begin, target)
    
    return answer
