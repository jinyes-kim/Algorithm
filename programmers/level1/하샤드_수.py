def solution(x):
    num = [int(x) for x in str(x)]
    dummy = sum(num)

    if int(x) % dummy == 0:
        return True
    return False
