"""
Q. 정렬된 배열에서 절대값으로 치환했을 때의 원소는 몇개인가?

전체 리스트에 map으로 abs 먹이고 set으로 중복제거해서 리턴

"""

def solution(A):
    A = list(map(abs, A))
    A_set = set(A)
    return len(A_set)
