"""
순열 - 1 ~ N까지 수가 빠짐없이 존재해야 한다.

1단계 - 파라미터 리스트의 길이를 받아서 지표로 삼을 집합을 생성한다. 
	1부터 시작하고 길이가 최댓값이 되므로 1~length+1 이 범위가 된다

2단계 - 이때 생성한 지표 집합의 길이가 파라미터 리스트이 길이와 다르면 요소가 비어있는 것이므로 0 리턴

3단계 - 길이가 같다면 배열 A를 집합인 check_list에 추가한다. 
	지표로 만든 dummy는 순열 지표이므로 이와 같으면 1을 리턴


"""

def solution(A):
    length = len(A)
    dummy = set([x for x in range(1, length+1)])    # indicator

    if len(dummy) != length:
        return 0

    check_list = set()
    for num in A:
        check_list.add(num)

    if check_list == dummy:
        return 1

    return 0