def solution(price, money, count):
    answer = 0
    cost= 0
    for i in range(1,count+1):
        cost+=price*i
    answer=money-cost
    return -answer if answer<0 else 0