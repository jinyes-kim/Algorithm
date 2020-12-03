def solution(s):
    alphabet_list = [x for x in s]
    alphabet_list.sort(reverse=True)
    answer = ''.join(alphabet_list)
    
    return answer