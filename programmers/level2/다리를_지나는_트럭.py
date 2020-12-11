def solution(bridge_length, weight, truck_weights):
    answer = 1
    bridge_queue = []
    current_weight = 0
    number_of_truck = 0

    while True:
        try:
            if current_weight + truck_weights[0] <= weight:
                current_weight += truck_weights[0]
                bridge_queue.append([truck_weights[0], bridge_length])
                number_of_truck += 1
                truck_weights.pop(0)
        except:
            answer += bridge_queue[-1][1]
            return answer

        complete = []
        for idx in range(number_of_truck):
            bridge_queue[idx][1] -= 1
            if bridge_queue[idx][1] == 0:
                complete.append(idx)

        for idx in complete:
            current_weight -= bridge_queue[idx][0]
            number_of_truck -= 1
            bridge_queue.remove(bridge_queue[idx])

        answer += 1

    return answer


#print(solution(2, 10, [7,4,5,6]))

"""
다리에 트럭이 몇개가 올라갈 수 있는지가 포인트

1. 트럭의 무게합이 다리의 하중보다 작거나 같으면 큐에 [무게, 길이] 추가
    - 트럭의 개수 += 1
    - 트럭의 총 무게 += 무게
    
   *- 만약 더 이상 트럭이 없다면 리스트 인덱싱 에러가 난다.
    - 위 상황이면 마지막 트럭이 다리 위에 있으므로 마지막 트럭의 길이(시간)을 추가하고 종료
    
2. 1번이 끝나면 큐에서 각 요소마다 길이(시간) -= 1

3. 각 트럭마다 길이(시간)이 0이 되었는지 검사한다.
    - 0이 되었다면 다리를 건넌 것이므로
     (1). 큐에서 제거
     (2). 현재 트럭의 총 무게에서 제거
     (3). 현재 다리 위에 있는 트럭의 개수 -= 1

"""
