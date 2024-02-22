def solution(ingredient):
    answer = 0
    ## 알고리즘: 리스트 내에서 특정 순서를 갖는 리스트 찾아내기
    # 1,2,3,1을 찾아내는 것
    # LSTM처럼 배치 사이즈를 4로 해서 한번 만들어볼까?
#     batch_size=4
#     ingredient_combi=[]
#     for i in range(0,len(ingredient)-batch_size+1):
#         c=[]
#         for j in range(i,i+batch_size):
#             c.append(ingredient[j])
#         ingredient_combi.append(c)
    
#     # print(ingredient_combi)
#     answer=ingredient_combi.count([1,2,3,1])
    ## 중간에 1231이 빠지고 다시 1231이 만들어지는 동적 과정을 고려하지 못해서 33퍼만 성공함..
    
    ## 문자열로 바꿔서 해보자
    
    # ingredient_str=''.join(list(map(str,ingredient)))
    # while True:
    #     if ingredient_str.find('1231')==-1:
    #         break
    #     else:
    #         answer+=1
    #         ingredient_str=ingredient_str.replace('1231','')

    
    ### 리스트의 특정위치의 값을 조회, 제거하고, 앞으로 땡겨야함.
    stack=[]
    for i,v in enumerate(ingredient):
        stack.append(v)
        if len(stack)>=4:
            check=stack[-4:]
            if check == [1,2,3,1]:
                answer+=1
                for _ in range(4):
                    stack.pop()
            
    return answer