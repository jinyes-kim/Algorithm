def solution(brown, yellow):
    height = 1
    width = yellow // height

    while height <= width:
        if yellow % height == 0:
            if (yellow // height) * 2 + (height * 2) + 4 == brown:
                break

        height += 1
        width = yellow // height

    return [width+2, height+2]


"""
풀이요약

노란 타일이 핵심이다. 노란 타일의 개수 그리고 층 수에 따라서 갈색 타일의 개수가 정해진다
노란 타일이 1층, 2층, 3층 일때 필요한 갈색 타일의 개수를 공식화 하고 인풋으로 들어온
갈색 타일의 개수와 같으면 해당 층수가 전체 카펫의 높이가 된다. 

노란색 타일의 개수에서 높이를 나눠준 것이 너비가 된다. 
너비와 높이에 +2 씩 붙이면 전체 카펫의 가로 x 세로 가 된다.

"""