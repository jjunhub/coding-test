from heapq import heapify, heappop, heappush
def solution(jobs):
    numOfJobs = len(jobs)
    currentTime = 0
    totalWaitingTime = 0
    heapify(jobs)
    # print(f'currentT = {currentTime}, inT = 0, workT = 0')
    while jobs:
        # print(jobs)
        
        # 현재 시간이 가장 앞서 있는 작업의 요청 시간보다 작다면,
        
        if currentTime < jobs[0][0]:
            # 그 시간까지 기다려야한다.
            currentTime = jobs[0][0]
        
        # 만약 현재 시간에서 대기하고 있는 jobs들이 2개 이상이라면, 가장 짧은 것을 먼저 진행한다.
        if len(jobs) >= 2 and jobs[0][0] <= currentTime and jobs[1][0] <= currentTime :
            waitingJobs = []
            minWorkTime = jobs[0][1]
            flag = 0
            while jobs and jobs[0][0] <= currentTime :
                waitingJobs.append(heappop(jobs))
            
            # print(f'waitingJobs = {waitingJobs}')
            for index, job in enumerate(waitingJobs):
                if job[1] < minWorkTime :
                    minWorkTime = job[1]
                    flag = index
                    
            inTime, workTime = waitingJobs.pop(flag)
            waitingTime = currentTime - inTime + workTime
            currentTime += workTime
            totalWaitingTime += waitingTime
            
            for job in waitingJobs:
                heappush(jobs, job)
            
        # 대기하고 있는 것이 1개라면,
        else :
            inTime, workTime = heappop(jobs)
            waitingTime = currentTime - inTime + workTime
            currentTime += workTime
            totalWaitingTime += waitingTime
            
        # print(f'currentT = {currentTime}, inT = {inTime}, workT ={workTime}')
        # print(f'totalWaitingT = {totalWaitingTime}')
        
    return int(totalWaitingTime / numOfJobs)

# print('--')
# jobs = [[0,4], [1,3], [2,2]]
# print(solution(jobs))
# print('--')
