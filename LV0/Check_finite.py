# 두 정수 a와 b가 매개변수로 주어질때 a/b가 유한소수이면 1을 무한소수라면 2를 return하는 함수를 작성하시오.
# 제한사항
# a와 b는 1 이상 1,000 이하의 정수이다.

from math import gcd

def solution(a,b):
    gcd_ab = gcd(a,b)
    if gcd_ab != 1:
        a //= gcd_ab
        b //= gcd_ab
    while b >= 2:
        if b % 2 == 0:
            b = int(b / 2)
        else:
            break
    while b >= 5:
        if b % 5 == 0:
            b = int(b / 5)
        else:
            break
    
    if b == 1:
        return 1
    return 2
        
print(solution(7,20)) # 1
print(solution(12, 21)) # 2
