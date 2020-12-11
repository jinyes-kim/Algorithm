# Queue
def solution(progresses, speeds):
    answer = []
    length = len(progresses)
    work_day = []

    for idx in range(length):
        work = 100 - progresses[idx]
        day = work / speeds[idx]

        if day % 1 != 0:
            day += 1

        work_day.append(int(day))

    while work_day:
        deployment = 0
        pivot = work_day[0]

        for value in work_day:
            if value <= pivot:
                deployment += 1
            else:
                break

        answer.append(deployment)
        work_day = work_day[deployment:]

    return answer


#O(N) 풀이
def solution(progresses, speeds):
    answer = []
    length = len(progresses)

    for idx in range(length):
        work = (100 - progresses[idx]) / speeds[idx]
        if work % 1 != 0:
            work += 1
        work = int(work)

        if idx == 0:
            pivot = work
            deployment = 1
        elif pivot < work:
            pivot = work
            answer.append(deployment)
            deployment = 1
        else:
            deployment += 1

    answer.append(deployment)
    return answer