def solution(s):
    try:
        s = int(s)
    except:
        return False
    
    length = len(str(s))
    
    if length == 4 or length == 6:
        return True
    
    return False