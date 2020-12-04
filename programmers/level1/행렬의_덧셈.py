def solution(arr1, arr2):
    answer = []
    for length in range(len(arr1)):
        dummy = []
        for idx in range(len(arr1[0])):
            dummy.append(arr1[length][idx] + arr2[length][idx])
        answer.append(dummy)
    return answer
