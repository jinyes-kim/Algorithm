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