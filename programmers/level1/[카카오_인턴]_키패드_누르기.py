def solution(numbers, hand):
    answer = ''
    left_hand = '*'
    right_hand = '#'
    only_left = (1, 4, 7)
    only_right = (3, 6, 9)
    keypad = {'1': {'2': 1, '5': 2, '8': 3, '0': 4},
              '2': {'2': 0, '5': 1, '8': 2, '0': 3},
              '3': {'2': 1, '5': 2, '8': 3, '0': 4},
              '4': {'2': 2, '5': 1, '8': 2, '0': 3},
              '5': {'2': 1, '5': 0, '8': 1, '0': 2},
              '6': {'2': 2, '5': 1, '8': 2, '0': 3},
              '7': {'2': 3, '5': 2, '8': 1, '0': 2},
              '8': {'2': 2, '5': 1, '8': 0, '0': 1},
              '9': {'2': 3, '5': 2, '8': 1, '0': 2},
              '0': {'2': 3, '5': 2, '8': 1, '0': 0},
              '*': {'2': 4, '5': 3, '8': 2, '0': 1},
              '#': {'2': 4, '5': 3, '8': 2, '0': 1}
              }

    for num in numbers:
        if num in only_left:
            answer += 'L'
            left_hand = num
        elif num in only_right:
            answer += 'R'
            right_hand = num
        else:
            left_count = keypad[str(left_hand)][str(num)]
            right_count = keypad[str(right_hand)][str(num)]

            if left_count < right_count:
                answer += 'L'
                left_hand = num
            elif right_count < left_count:
                answer += 'R'
                right_hand = num
            else:
                if hand == 'left':
                    answer += 'L'
                    left_hand = num
                else:
                    answer += 'R'
                    right_hand = num

    return answer


"""
* 2, 5, 8, 0 을 누를 때 왼손, 오른손 중 어느 쪽으로 눌러야 손가락이
적게 움직이는 가 계산해야하는 것이 포인트

처음엔 bfs 방식으로 접근했으나, 키패드의 특성상 숫자가 작다는 것을 고려하면
전체 키패드에서 2, 5, 8, 0 을 접근하기 위한 최단 거리를 메모리 상에 먼저 띄어두고
계산하는 게 더 효율적이라고 판단
"""