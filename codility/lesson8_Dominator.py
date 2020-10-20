"""
가장 많이 나온 원소의 인덱스 전부 반환
없으면 -1 반환

문제에서는 절반 이상이라고 하는데,
20개 중에서 10개 이상이 아니라 11개 이상으로 풀어야한다.

"""
def solution(A):
    tmp_list = list(set(A))
    length = len(A)

    # 1개만 존재하는 케이스
    if len(tmp_list) == 1:
        return 0

    # number count
    indicator = {}
    for num in A:
        if num in indicator:
            indicator[num] += 1
        else:
            indicator[num] = 1

    # check dominator
    half = int((length / 2) + 1)

    candidate_list = []
    for num, count in indicator.items():
        if count >= half:
            candidate_list.append((num, count))
    # no dominator option
    if len(candidate_list) == 0:
        return -1

    candidate_list.sort(key=lambda x: x[1])
    for idx, num in enumerate(A):
        if num == candidate_list[-1][0]:
            return idx

