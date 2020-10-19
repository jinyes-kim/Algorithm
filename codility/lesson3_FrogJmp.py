# math 라이브러리 사용 코드
import math

def solution(X, Y, D):
    value = Y - X
    answer = value / D
    return math.ceil(answer)



# 생짜 코드
def solution(X, Y, D):
    value = Y - X
    answer = value / D

    if answer % 1 != 0:
        return int(answer) + 1
    else:
        return int(answer)