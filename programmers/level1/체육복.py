def solution(n, lost, reserve: list):
    answer = n - len(lost)
    enroll_fail_list = []

    # remove self reserve
    for student in lost:
        if student in reserve:
            reserve.remove(student)
            answer += 1
        else:
            enroll_fail_list.append(student)

    for student in enroll_fail_list:
        if student-1 in reserve:
            reserve.remove(student-1)
            answer += 1
        elif student+1 in reserve:
            reserve.remove(student+1)
            answer += 1

    return answer


"""
1. 초기 개수 = n - len(lost)
2. 도난 당한 학생 중 여벌이 있는 케이스 체크 answer += 1
3. 도난 당하고 여벌이 없는 학생 중 빌릴 수 있는 케이스 체크 answer += 1

"""