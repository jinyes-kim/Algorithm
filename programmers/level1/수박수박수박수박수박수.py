def solution(n):
    word = ('수', '박')
    answer = ''.join([word[x % 2] for x in range(n)])
    
    return answer