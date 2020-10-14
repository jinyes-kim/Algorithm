def solution(bridge_length, weight, truck_weights):
    time = 0
    queue = truck_weights
    check_weight = 0
    driving_truck_list = []

    while True:
        time += 1

        if queue and check_weight + queue[0] <= weight:
            check_weight += queue[0]
            driving_truck_list.append([queue.pop(0), bridge_length])

        #print(time, check_weight, driving_truck_list, queue)
        driving_truck_list = list(map(lambda x: [x[0], x[1]-1], driving_truck_list))

        # end condition
        if not driving_truck_list:
            break

        if driving_truck_list[0][1] == 0:
            done_weight = driving_truck_list.pop(0)
            check_weight -= done_weight[0]

    return time



# sample

#bridge_length = 100
#weight = 100
#truck_weight = [10,10,10,10,10,10,10,10,10,10]
#print(solution(bridge_length, weight, truck_weight))



"""
0. 시간 ++
1. 새 트럭이 추가되는 경우 다리가 하중을 버틸 수 있는가? 
2-1. 버틸 수 있다면 drivig_truck_list 에 추가
2-2. 버틸 수 없다면 패스
3. driving_truck_list에 있는 트럭들의 시간을 --
4. 만약 driving_truck_list에 있는 요소의 시간이 0이 되면 큐잉, 해당 원소를 checker_weight에서 빼서 무게 업데이트
5. 위 과정을 반복하면서 만약 driving_truck_list에 아무 것도 없게되면 연산을 종료 

"""



"""
시뮬레이션 문제라서 트럭을 객체로 만들어서 진행할 수도 있고, 학습에 더 좋은 방법일 것 같은데,
2차원 리스트로 구현하는 게 더 간편해서 위와 같이 구현했다.
정말 간단하지만 최적화를 위해서 더 생각을 해봐야할 것 
"""
