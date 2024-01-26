def solution(chicken):
    service = 0
    coupons = chicken

    while coupons >= 10:
        service += coupons // 10
        coupons = coupons // 10 + coupons % 10

    return service