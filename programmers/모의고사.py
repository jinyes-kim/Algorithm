def solution(answers):
    score_list = [0, 0, 0]
    length = len(answers)
    first_omr = first_man(length)
    second_omr = second_man(length)
    third_omr = third_man(length)

    for num in range(length):
        question = answers[num]
        if first_omr[num] == question:
            score_list[0] += 1
        if second_omr[num] == question:
            score_list[1] += 1
        if third_omr[num] == question:
            score_list[2] += 1

    maximum_score = max(score_list)
    answer = []
    for n in range(3):
        if score_list[n] == maximum_score:
            answer.append(n+1)

    return answer


def first_man(length):
    res = []

    for n in range(0, length):
        res.append((n % 5)+1)
    return res


def second_man(length):
    res = []

    for n in range(0, length+1):
        if len(res) >= length:
            break

        num = (n % 5) + 1
        if num == 2:
            continue
        else:
            res.append(2)
            res.append(num)

    return res


def third_man(length):
    res = [3, 3]

    for n in range(0, length+1):
        if len(res) >= length:
            break

        num = (n % 5) + 1
        if num == 3:
            continue
        else:
            res.extend([num, num])
            if num == 5:
                res.extend([3, 3])

    return res