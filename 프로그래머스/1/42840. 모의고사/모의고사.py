# def solution(answers):
#     ## 수포자들의 답과 비교를 위하여 문자열로 변환
#     answers=''.join([str(n) for n in answers])

#     ## 수포자들의 알고리즘
#     # 1: 12345 반복 5
#     # 2: 21232425 반복 8 
#     # 3: 3311224455 반복 10
    
#     ## 수포자들의 반복을 정확히 answers의 길이만큼만 반복시켜주어야함
#     supoza1='12345'*(len(answers)//5)+'12345'[:len(answers)%5]
#     supoza2='21232425'*(len(answers)//8)+'21232425'[:len(answers)%9]
#     supoza3='3311224455'*(len(answers)//10)+'3311224455'[:len(answers)%10]
    
#     ## answers와 supoza n을 통째로 비교해서, True들만 더해주면 어떨까
#     score1=sum([i==j for i,j in zip(list(supoza1),list(answers))])
#     score2=sum([i==j for i,j in zip(list(supoza2),list(answers))])
#     score3=sum([i==j for i,j in zip(list(supoza3),list(answers))])
#     scores=[score1,score2,score3]
#     ## scores를 순회하면서 최대값과 같은 값의 인덱스+1(학생번호)을 리턴
#     return ([i+1 for i,v in enumerate(scores) if v==max(scores)])


## gpt코드
def solution(answers):
    # 수포자들의 답을 미리 계산한 패턴으로 생성
    supoza1 = [1, 2, 3, 4, 5] * ((len(answers) + 4) // 5)
    supoza2 = [2, 1, 2, 3, 2, 4, 2, 5] * ((len(answers) + 7) // 8)
    supoza3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * ((len(answers) + 9) // 10)

    # 정답과 수포자들의 답을 비교하여 점수 계산
    scores = [sum(i == j for i, j in zip(supoza1, answers)),
              sum(i == j for i, j in zip(supoza2, answers)),
              sum(i == j for i, j in zip(supoza3, answers))]

    # 가장 높은 점수를 받은 수포자들의 번호 반환
    max_score = max(scores)
    return [i + 1 for i, v in enumerate(scores) if v == max_score]