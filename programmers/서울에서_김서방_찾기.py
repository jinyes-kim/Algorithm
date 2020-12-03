def solution(seoul):
    for idx, name in enumerate(seoul):
        if name == "Kim":
            return "김서방은 {}에 있다".format(idx)
