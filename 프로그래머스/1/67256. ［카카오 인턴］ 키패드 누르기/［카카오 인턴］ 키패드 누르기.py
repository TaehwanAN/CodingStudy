def solution(numbers, hand):
    answer = ''
    ## 알고리즘 분석:
    # 왼손과 오른손의 현재 위치를 튜플로 저장해둘 변수 필요.
    # 전체 번호판의 구조: 이중 리스트(4행 3열)
    # 번호의 위치를 해시구조로 저장
    # 거리를 구할 때는 피타고라스의 정리를 이용하자.
    # 순회대상: numbers
    ## 매 순회시:
    # 어떤 손가락 사용할지 비교 -> 사용한 손가락을 결과에 붙이기 -> 사용: 그 손가락의 위치 갱신
    
    keypad_list=[[1,2,3],[4,5,6],[7,8,9],['#',0,'*']]
    keypad_dic=dict()
    for row, l in enumerate(keypad_list):
        for col, k in enumerate(l):
            # print((row,col))
            keypad_dic[k]=[row,col]

    left_loc=(3,0)
    right_loc=(3,2)
    
    for n in numbers:
        left_dist=0
        right_dist=0
        if n in [1,4,7]:
            answer+='L'
            left_loc=keypad_dic[n]
        elif n in [3,6,9]:
            answer+='R'
            right_loc=keypad_dic[n]
        else:
            left_dist=abs(keypad_dic[n][0]-left_loc[0])+abs(keypad_dic[n][1]-left_loc[1])
            right_dist=abs(keypad_dic[n][0]-right_loc[0])+abs(keypad_dic[n][1]-right_loc[1])
            # print(keypad_dic[n])
            # print(left_dist,right_dist)
            if left_dist<right_dist:
                answer+='L'
                left_loc=keypad_dic[n]
            elif left_dist>right_dist:
                answer+='R'
                right_loc=keypad_dic[n]
            else:
                if hand=='left':
                    answer+='L'
                    left_loc=keypad_dic[n]
                elif hand=='right':
                    answer+='R'
                    right_loc=keypad_dic[n]
    return answer