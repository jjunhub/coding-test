import sys
input = sys.stdin.readline

N = int(input())
meetings = []
for _ in range(N):
  meeting = list(map(int, input().split()))
  meetings.append(meeting)

meetings = sorted(meetings, key= lambda x : (x[1], x[0]))

startTime = meetings[0][0]
endTime = meetings[0][1]
num = 1
meetingNum = 1

while num < N:
  if meetings[num][0] < endTime:
    num += 1
  else :
    endTime = meetings[num][1]
    meetingNum += 1
    num += 1

print(meetingNum)