def solution(answers):
    answer = []
    student_score = [0, 0, 0]
    length = len(answers)

    first_student = first_man(length)
    second_student = second_man(length)
    third_student = third_man(length)

    for idx, n in enumerate(answers):
        if n == first_student[idx]:
            student_score[0] += 1
        if n == second_student[idx]:
            student_score[1] += 1
        if n == third_student[idx]:
            student_score[2] += 1

    max_value = max(student_score)
    for idx in range(3):
        if student_score[idx] == max_value:
            answer.append(idx+1)

    return answer


def first_man(length):
    result = []

    for n in range(0, length):
        result.append((n % 5)+1)

    return result


def second_man(length):
    result = []

    for n in range(0, length):
        if len(result) >= length:
            break

        num = (n % 5) + 1
        if num == 2:
            continue
        else:
            result.append(2)
            result.append(num)

    return result


def third_man(length):
    result = [3, 3]

    for n in range(0, length):
        if len(result) >= length:
            break

        num = (n % 5) + 1

        if num == 3:
            continue
        else:
            result.extend([num, num])
            if num == 5:
                result.extend([3, 3])

    return result


"""
1. 3가지 케이스 함수로 작성
2. answers 리스트와 비교하며 답안 체크, 스코어 리스트에 맞은 개수 체크
3. 최고점 찾기
4. 1번 학생부터 최고점인지 검사, 최고점이면 answer 리스트에 추가
"""