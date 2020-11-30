# 라이브러리 활용
import collections as col

def solution(participant, completion):
    return list(col.Counter(participant) - col.Counter(completion))[0]



# hard coding

def solution(participant, completion):
    result = {}

    for completion_member in completion:
        try:
            result[completion_member] += 1
        except:
            result[completion_member] = 1

    for participant_member in participant:
        try:
            result[participant_member] -= 1
        except:
            return participant_member

    for check in result:
        if result[check] < 0:
            return check


"""
TC에 안 걸리려면 O(N)으로 풀어야한다.

1. result 딕셔너리에 completion 멤버 추가
    * 이때 동명이인 처리를 위한 작업이 필요한데, 예외처리 구문을 활용해서
        시간복잡도를 최적화할 수 있다.

2. partition 멤버를 키로 삼아 result 딕셔너리에서 매칭후 밸류 -= 1
    * 키 에러가 나면 해당 멤버는 완주 목록에 없으므로 리턴
    
3. 2번에서 안 끝나는 경우 동명이인이 존재하므로 밸류가 마이너스인 키를 리턴
"""


