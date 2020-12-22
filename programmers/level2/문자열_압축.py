def solution(s):
    text_length = len(s)
    preprocessed = []

    for n in range(1, len(s)+1):
        count = 1
        text = ''
        dummy_text = ''
        mod = text_length % n
        for idx, pivot in enumerate(range(0, text_length-mod+1, n)):
            if idx == 0:
                dummy_text = s[pivot:pivot+n]
                continue

            if s[pivot:pivot+n] == dummy_text:
                count += 1
            else:
                if count < 2:
                    text += dummy_text
                else:
                    text += str(count) + dummy_text
                count = 1
                dummy_text = s[pivot:pivot+n]

        text += s[text_length-mod:text_length]
        preprocessed.append(text)

    preprocessed.sort(key=lambda x: len(x))
    return len(preprocessed[0])

#print(solution("abcabcabcabcdededededede"))

"""
0. n자리로 잘랐을 때 남는 나머지 문자열을 미리 빼둔다.
1. 정제한 문자열을 n자리씩 잘라가면서 같은지 검사한다.
2.  - 다르면 현재까지 카운팅한 숫자를 붙여서 text에 저장한다.
    - 같으면 카운팅

위 과정을 1~n자리까지 반복하고,
문자열을 담은 리스트를 길이를 기준으로 정렬한다.
"""
