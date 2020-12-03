def solution(s):
    transfer_list = []

    for word in s.split(' '):
        new_word = ''
        for idx, alphabet in enumerate(word):
            if idx % 2 == 0:
                new_word += alphabet.upper()
            else:
                new_word += alphabet.lower()

        transfer_list.append(new_word)
        answer = ' '.join(transfer_list)

    return answer
