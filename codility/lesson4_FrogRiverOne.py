"""
타겟 밸류 X를 위해 1~X까지 이어지는 수가 완성될 때의
인덱스를 리턴하는 문제

1단계 - 지표로 삼을 set, 프로그 set 생성
2단계 - 프로그 set에 원소 추가하면서 지표와 같은지 확인
"""

def solution(X, A):
    bridge = set([i for i in range(1, X+1)])
    frog_step = set()
    
    for idx, num in enumerate(A):
        frog_step.add(num)
        if frog_step == bridge:
            return idx

    return -1