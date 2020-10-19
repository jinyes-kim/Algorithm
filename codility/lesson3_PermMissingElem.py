"""
등차수열에서 빠진 수 찾기
배열에서 숫자는 정렬된 상태가 아니다.

1단계 length+1 만큼 배열 만들기
2단계 배열 순회하면서 체크
3단계 0인 배열 리턴

O(N)

"""
def solution(A):
    length = len(A)
    length_list = [0 for _ in range(length+1)]
    
    for num in A:
        length_list[num-1] = 1
    
    for i, num in enumerate(length_list):
        if num == 0:
            return i+1