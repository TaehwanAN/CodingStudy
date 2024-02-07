# def solution(phone_book):
#     ## 알고리즘 고민
#     # PHONE 북의 가장 긴 원소의 길이부터 시작하여, 가장 짧은 원소까지 반복.
#     # 모든 원소를 한 자리씩 다 줄여나가기
#     # 원래 리스트의 길이와 SET에 넣은 길이가 다르면 접두사 존재한다는 의미 => FALSE 반환
#     answer = True

#     for i in range(len(max(phone_book)),len(min(phone_book))-1,-1):
#         phone_book=list(map(lambda x: x[:i], phone_book))
#         # print(phone_book)
#         if len(phone_book)!=len(set(phone_book)):
#             return False
#     return answer


### 테스트 케이스 11 15 19 실패, 효율성 테스트 4 실패

def solution(phone_book):
    ## gpt로부터 받은 코드, 알고리즘 이해
    # 전화번호부를 집합으로 변경하여 중복을 일단 제거한다. 
    # 전화번호부 집합에서 원소를 가져와서 그 원소 기준 접두사를 추출한뒤, 그 접두사 자체를 값으로 갖는 다른 원소가 존재하는 경우 False를 반환한다.
    phone_set = set(phone_book)  # 중복 제거
    for number in phone_book:
        for i in range(1, len(number)):
            prefix = number[:i] # 접두사 추출
            if prefix in phone_set and prefix != number: # 다른 원소와 동일한지 검토
                return False
    return True