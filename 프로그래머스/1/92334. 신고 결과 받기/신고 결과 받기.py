from collections import defaultdict

def solution(id_list, report, k):
    reported_set = defaultdict(set)
    report_success_count = defaultdict(int)
    
    for event in report:
        blocker, blocked = event.split(" ")
        reported_set[blocked].add(blocker)
    
    for blocked in id_list:
        if (len(reported_set[blocked])) >= k:
            for blocker in reported_set[blocked]:
                report_success_count[blocker] += 1
    
    answer = []
    for _id in id_list:
        answer.append(report_success_count[_id])
    
    return answer