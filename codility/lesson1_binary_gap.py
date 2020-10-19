def solution(N):
    # step 1
    value = N
    binary = ''
    
    while value != 1:
        mod = value % 2
        binary += str(mod)
        
        value = value // 2
        if value == 1:
            binary += str(value)
    
    binary = binary[::-1]
    
    # step 2
    maximum = 0
    dummy = 0
    for zero in binary:
        if zero == '1':
            if maximum < dummy:
                maximum = dummy
            dummy = 0
            
        else:
            dummy += 1
            
    return maximum
        
    



"""

1단계 - 이진수 변환
    

2단계 - binary gap searching
    0개수 세고 초기화하면서 최대값 업데이트,
     맥시멈 리턴하면 O(N)

"""