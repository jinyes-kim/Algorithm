def solution(strings, n):
    subset = set()
    word_dict = {}
    answer = []

    for alphabet in strings:
        subset.add(alphabet[n])

    subset = sorted(list(subset))

    for alphabet in subset:
        for word in strings:
            if word[n] == alphabet:
                try:
                    word_dict[word[n]].append(word)
                except:
                    word_dict[word[n]] = [word]

    for alphabet in subset:
        sub_list = sorted(word_dict[alphabet])
        answer.extend(sub_list)

    return answer


"""
print(solution(["abce", "abcd", "cdx"], 2))

* sort에 람다옵션 줘서 푸려다가 실패

풀이 방법
1. 정렬하고자 하는 인덱스 알파뱃을 땡겨와서 리스트 적재 후 정렬
2. strings 리스트에서 n번째 인덱스가 일치하는 것끼리 부분집합 생성 (딕셔너리로 구현)
3. 부분집합 정렬
4. 1번에서 만든 리스트의 요소 순서대로 루프가 돌아가므로 그대로 answer 리스트에 적재


더 효율적인 코드 고민해보기
"""
