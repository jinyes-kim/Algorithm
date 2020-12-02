def solution(arr):
    answer = [arr[0]]
    for n in arr:
        if n != answer[-1]:
            answer.append(n)
            
    return answer

"""
연속으로 나오는 숫자면 패스
아니면 리스트에 추가
"""