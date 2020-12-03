import math


def solution(n):
    if is_sqrt(n):
        tmp = int(math.sqrt(n)) + 1
        return tmp * tmp
    return -1


def is_sqrt(number):
    if math.sqrt(number) % 1 == 0:
        return True
    return False

