"""
피벗 왼쪽과 오른쪽을 나눠서 더하고 뺀 절대값
중에서 가장 작은 값

"""
def solution(A):
    length = len(A)
    left_list, right_list = [], []
    left, right = 0, 0
    answer = float('inf')

    # left 순방향 누적합
    # right 역방향 누적합
    for idx in range(length-1):
        left += A[idx]
        right += A[length - idx - 1]
        left_list.append(left)
        right_list.append(right)

    right_list = right_list[::-1]

    for idx in range(length-1):
        new_value = abs(left_list[idx] - right_list[idx])
        if new_value < answer:
            answer = new_value

    return answer