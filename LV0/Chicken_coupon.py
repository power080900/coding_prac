# 치킨을 한마리 시키면 쿠폰을 한장 주는 치킨 집이 있다. 시켜먹은 chicken의 수가 매개변수로 주어질 때, 최대로 받을수 있는 서비스 치킨의 수를 return하는 함수를 작성하시오.
# 제한사항
# chicken은 0 이상 1,000,000 이하인 정수이다.
# 쿠폰 10장당 치킨 1마리가 서비스로 나오며 서비스 치킨에도 쿠폰이 나온다.

def solution(chicken):
    answer = 0
    coupon = chicken

    while coupon >= 10:
        eaten = coupon // 10
        answer += eaten
        coupon = coupon % 10 + eaten

    return answer

print(solution(100)) # 11
print(solution(1081)) # 120