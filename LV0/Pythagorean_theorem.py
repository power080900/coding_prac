# 직각삼각형의 한 변 a와 빗변 c가 매개변수로 주어질 때, 다른 한 변의 길이의 제곱을 return하는 함수를 작성하시오.
# 제한사항
# a는 1 이상 c 이하인 자연수이다.
# c는 a 이상 100 이하인 자연수이다.

def solution(a, c):
    return c ** 2 - a ** 2

q1_a = 3
q1_c = 5

print(solution(q1_a, q1_c)) # 4