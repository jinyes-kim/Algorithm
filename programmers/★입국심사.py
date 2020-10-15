def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n

    while left <= right:
        mid = (left + right) // 2
        costumer = 0

        print(left, right, mid)
        for time in times:
            costumer += mid // time
            if costumer >= n:
                break

        if costumer >= n:
            answer = mid
            right = mid-1

        else:
            left = mid+1

    return answer


"""
이분탐색을 어떻게 활용하는지 잘 보여주는 문제다.
답안 참고를 했으므로 다시 생각해보기

"""