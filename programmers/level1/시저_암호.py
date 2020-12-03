import string


def solution(s, n):
    answer = ''
    lower_list = string.ascii_lowercase
    upper_list = string.ascii_uppercase

    for alphabet in s:
        if alphabet == ' ':
            answer += ' '
        elif alphabet.islower():
            pivot = (lower_list.index(alphabet)+n) % 26
            answer += lower_list[pivot]
        elif alphabet.isupper():
            pivot = (upper_list.index(alphabet)+n) % 26
            answer += upper_list[pivot]

    return answer


"""
string 내장 라이브러리에 lower alphabet, upper alphabet 리스트가
있으므로 이를 활용한다

알파뱃 개수는 26개

"""

