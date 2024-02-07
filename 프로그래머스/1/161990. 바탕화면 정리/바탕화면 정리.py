    ## 알고리즘 분석
    # wallpaper는 리스트로, 그 원소는 문자열로 주어진다.
    # 리스트를, 그리고 문자열을 순회하면서, #의 (row,col) 좌표를 튜플 형태로 저장한다.
    # 예) [(0,1),(1,2),(2,3)]
    # 이 좌표들은 각 파일의 좌상단 모서리의 위치이다. 그러므로 좌하단, 우상단, 우하단 값은 다르게 정의된다.
    # 좌상단(row,col), 좌하단(row,col+1), 우상단(row+1,col), 우하단(row+1,col+1)
    
def solution(wallpaper):
    answer=[]
    coordinate={'row':[], 'col':[]}
    for row, wall in enumerate(wallpaper):
        for col, s in enumerate(wall):
            if s=='#':
                coordinate['row'].append(row)
                coordinate['col'].append(col)
    # print(coordinate)
    # print(min(coordinate['row']))


    answer.append(min(coordinate['row']))
    answer.append(min(coordinate['col']))
    answer.append(max(coordinate['row'])+1)
    answer.append(max(coordinate['col'])+1)
    return answer