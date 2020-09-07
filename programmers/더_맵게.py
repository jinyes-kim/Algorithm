import heapq


def solution(scoville, K):
    queue = []

    for score in scoville:
        heapq.heappush(queue, score)

    count = 0
    while queue:
        if len(queue) == 1 and queue[0] < K:
            return -1
        if queue[0] >= K:
            return count

        first_min = heapq.heappop(queue)
        second_min = heapq.heappop(queue)
        new_cooking = first_min + (second_min * 2)

        heapq.heappush(queue, new_cooking)
        count += 1