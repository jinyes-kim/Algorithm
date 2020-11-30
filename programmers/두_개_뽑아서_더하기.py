def solution(numbers):
    answer = set()
    length = len(numbers)
    numbers.sort()

    for x_idx in range(length-1):
        for y_idx in range(x_idx+1, length):
            value = numbers[x_idx] + numbers[y_idx]
            answer.add(value)

    answer = list(answer)
    answer.sort()
    return answer


"""
* 별도의 조건없이 배열 안에 있는 정수 두 개를 뽑아서 더하고 리스트에 추가한다.
  오름차순으로 정렬해서 리턴

순차탐색은 선택정렬 방식으로 

"""