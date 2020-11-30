def solution(array, commands):
    answer = []

    for i, j, k in commands:
        partition_list = array[i-1: j]
        partition_list.sort()
        answer.append(partition_list[k-1])

    return answer
