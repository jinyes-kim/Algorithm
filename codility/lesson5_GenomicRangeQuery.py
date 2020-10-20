"""
    dna = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

이고 입력으로 주어지는 스트링과 배열 두개를 이용해서 스트링의 부분집합을
생성하고, 해당 부분집합에 등장하는 알파뱃의 가중치가 가장작은 것이 해당 
문자열의 값이 된다.

단 앞에 방어 코드로, 입력으로 주어지는 문자열이 모두 같은 경우게 관해서 처리해준다.
"""
def solution(S, P, Q):
    length = len(P)
    dna = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

    if len(set(S)) == 1:
        return [dna[S[0]] for _ in range(length)]

    answer_list = []
    for idx in range(length):
        start = P[idx]
        end = Q[idx] + 1
        word = S[start:end]

        if 'A' in word:
            answer_list.append(1)
        elif 'C' in word:
            answer_list.append(2)
        elif 'G' in word:
            answer_list.append(3)
        else:
            answer_list.append(4)

    return answer_list