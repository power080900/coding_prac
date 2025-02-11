# 첫 달 저축금액을 start, 70만원 모일 때까지 저축금액을 before, 70만원 모인 후 저축금액을 after라고 할 때, 100만원을 모을 때까지 걸리는 개월수를 구하는 함수를 작성하시오.
# 제한사항
# start는 0 이상 99 이하이다.
# before는 1 이상 after 이하이다.
# after는 before 이상 25 이하이다.

def solution(start, before, after):
    month = 1
    money = start
    while money < 100:
        if money < 70:
            money += before
        else:
            money += after
        month += 1
    return month

q1_start = 28
q1_before = 6
q1_after = 8

print(solution(q1_start, q1_before, q1_after)) # 12