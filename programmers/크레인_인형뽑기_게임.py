def solution(board, moves):
    answer = 0
    bucket = []

    for idx in moves:
        for coordinates in board:
            if coordinates[idx - 1] != 0:
                bucket.append(coordinates[idx - 1])
                coordinates[idx - 1] = 0

                while pop_dolls(bucket):
                    bucket = bucket[:-2]
                    answer += 2

                break

    return answer


def pop_dolls(bucket):
    if len(bucket) < 2:
        return False

    if bucket[-1] == bucket[-2]:
        return True
    return False

"""
1. moves 요소를 순차적으로 get
2. board에서 요소가 가르키는 아이템 확인
3. 0이면 패스 / 0이 아니면 버킷에 적재
4. 적재한 아이템과 바로 이전 아이템이 같으면 아이템 두 개 삭제

4번 과정은 pop_dolls 라는 함수를 만들어서 따로 분리했음

"""