# def solution(number, limit, power):
#     answer = 0
#     ## 약수의 개수를 담기
#     ### 약수의 개수를 찾는 부분에서 시간복잡도가 너무 높은듯(테스트11번 부터 주르륵 시간초과 발생)
#     # div_list=[]
#     # for i in range(1,number+1):
#     #     cnt=0
#     #     for j in range(1,i+1):
#     #         if i%j==0:
#     #             cnt+=1
#     #     div_list.append(cnt)
#     # print(div_list)
    
#     ## 약수의 개수가 limit 초과하는지를 검토하고, 결과값에 div값들 추가해주기
#     for div in div_list:
#         if div>limit:
#             answer+=power
#             continue
#         else: 
#             answer+=div
#         # print(answer)
    
#     return answer

## gpt 코드: 시간복잡도 줄이기
def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        cnt = 0
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0: ## j가 i의 약수라면 개수 1증가
                cnt += 1
## 약수일 때, i를 j로 나눈 몫이 j가 아니라면, 약수가 하나 더 존재한다는 의미이므로 약수의 개수 1 또 증가
# 예: 2는 10의 약수. 10을 2로 나누면 5. 2와 5는 10의 약수 쌍임. 따라서 5에 해당하는 카운트 증가.
                if j != i // j:  # 중복 제거 
                    cnt += 1
## 따로 약수의 개수를 리스트로 담지 않고, 약수의 개수를 구한 뒤 바로 answer 증가 시켜줌
        if cnt > limit:
            answer += power
        else:
            answer += cnt
    return answer