# def solution(people,limit):
#     answer=0
#     aloneList=[]
#     minWeight=min(people)

#     # 일단 혼자만 타야하는 사람은 먼저 내보낸다.
#     while True:
#         if max(people)> (limit-min(people)):
#             answer+=1
#             people.remove(max(people))
#             # print(people)
#         else:
#             break


#     # while True:
#     #     boat=[]
#     #     while True:
#     #         boat.append(min(people))
#     #         people.remove(min(people))
#     #         print("boat",boat)
#     #         print("people",people)
#     #         if sum(people)+min(people)>limit:
#     #             break
#     #     print(answer)
#     #     answer+=1
#     #     if len(people)==0:
#     #         break


#     ## 알고리즘 고민
#     # 만약 다음 탈사람까지 더한 몸무게 합산이 보트 무게 제한을 넘기면,그 사람은 못탄채로 보트를 출발 시킨다. 
#     # 빈 보트에는 일단 제일 몸무게 적은 사람 부터 태운다. 그리고 무인도에서 그 사람을 제거한다. 
#     # 보트가 출발하면 정답 +1 해주고, 다음 새로운 보트가 들어온다. 
#     # 이 작업은 무인도에 남은 인간이 하나도 없을때 까지 반복된다.
#     ## 알고리즘 만들다 보니 min()활용할때 people이 빈 깡통이면 에러가 발생함.
#     # 그래서 무인도에 1명 남으면 그냥 그 사람을 혼자 태워서 보내버리고 정답 +1 해주고 while 문 종료 시켜버림.

#     # while len(people)>0:
#     #     boat=[]
#     #     while len(people)>0:
#     #         if (len(boat)==2 or (sum(boat)+min(people)>limit)):
#     #             break
#     #         boat.append(min(people)); people.remove(min(people));
#     #     answer+=1

#     return answer




## GPT 물어본 코드
def solution(people, limit):
    people.sort()
    answer = 0
    i, j = 0, len(people) - 1
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        answer += 1
    return answer
        