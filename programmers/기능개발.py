import math

def solution(progresses, speeds):
    length = len(speeds)
    answer = []
    tmp_list = []
    res = 1

    for i in range(length):
        progres = math.ceil((100 - progresses[i]) / speeds[i])
        tmp_list.append(progres)
        if i == 0:
            pivot = tmp_list[i]
        elif pivot < tmp_list[i]:
            pivot = tmp_list[i]
            answer.append(res)
            res = 1
        else:
            res += 1
    
    answer.append(res)
    return answer