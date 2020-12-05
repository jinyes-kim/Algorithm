def solution(dartResult):
    score_list = []
    bonus_dict = {'S': 1, 'D': 2, 'T': 3}
    option_dict = ('*', '#')
    score = ''

    for point in dartResult:
        if point.isdigit():
            score += point

        elif point in bonus_dict.keys():
            score_list.append(int(score) ** bonus_dict[point])
            score = ''

        elif point in option_dict:
            length = len(score_list)
            if point == '*':
                score_list[length-1] = score_list[length-1] * 2
                if length > 1:
                    score_list[length-2] = score_list[length-2] * 2

            elif point == '#':
                score_list[length-1] = -score_list[length-1]

            score = ''

    answer = sum(score_list)
    return answer

#print(solution('1D2S0T'))

"""
인풋은 점수|보너스|옵션 (단 옵션은 없을 수도 있다.)
점수는 0~10사이의 정수

1. 인풋이 숫자면 문자열로 붙여서 저장한다.
2. 만약 S, D, T에 해당하는 문자열이 들어오면 여태 저장한 스코어를 보너스에 맞춰 계산하고 적재
3. 옵션이 들어온다면 그에 맞는 행위를 한다.

    - * 이면 스코어를 저장한 인덱스와 바로 이전 인덱스의 값을 두 배로 늘린다.
        이때 첫 번째에서 스타 옵션을 받은 경우 첫 번째 스코어만 두 배
    
    - # 이면 받은 점수를 -로 변환한다.
"""