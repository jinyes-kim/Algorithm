def solution(n, lost, reserve):
    answer = 0
    removed_list = []
    
    for i in range(1, n+1):
        if i not in lost:
            removed_list.append(i)

    for n in range(1, n+1):
        if n not in removed_list:
            if n in reserve:
                reserve.remove(n)
                removed_list.append(n)

    for n in range(1, n+1):
        if n not in removed_list:
            if n-1 in reserve:
                reserve.remove(n-1)
                answer += 1
            elif n+1 in reserve:
                reserve.remove(n+1)
                answer += 1
            else:
                continue

        else:
            answer += 1

    return answer


#print(solution(5, [2, 4], [1,3,5]))


"""
풀이 요약

1. 체육복을 도난 당한 원소를 제거한 리스트 생성 -> removed_list
2. 도난 당한 원소가 reserve(여분) 리스트에 있는 경우 removed_list에 추가하고 reserve 에서는 삭제
3. 1~n 까지 순회, 만약 숫자가 removed_list에 없는 경우 도난 당한 케이스인데, 
    이때 n-1, n+1이 reserve에 있는 경우 체육복을 빌릴 수 있으므로 n-1 또는 n+1을 reserve에서 삭제하고 answer += 1
    숫자가 removed_list에 존재하는 경우에는 곧 바로 answer += 1

"""