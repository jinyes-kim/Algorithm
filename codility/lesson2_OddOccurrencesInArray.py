"""
배열에서 짝이 안 맞는 케이스 리턴

"""
def solution(A):
    fair_dict = dict()
    
    for num in A:
        if num not in fair_dict:
            fair_dict[num] = 1
        else:
            fair_dict[num] += 1
    
    for num, count in fair_dict.items():
        if count % 2 != 0:
            return num