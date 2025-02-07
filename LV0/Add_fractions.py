# 첫번째 분수의 분자 numer1, 분모 denom1, 두번째 분수의 분자 numer2, 분모 denom2를 입력받아 두 분수의 합을 기약분수로 구하는 프로그램을 작성하시오.
# 제한사항
# numer1, denom1, numer2, denom2는 1 이상 1000 이하의 자연수이다.

from math import gcd

def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    g = gcd(numer, denom)
    return [numer//g, denom//g]

print(solution(1,2,3,4)) # [5, 4]
print(solution(9,2,1,3)) # [29, 6]