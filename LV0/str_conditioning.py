# 두 정수 n,m과 문자열 ineq,eq가 주어질 때, 조건에 맞으면1 아니면 0을 retun하는 함수를 작성하시오.
# 제한사항
# n,m은 1이상 100이하의 자연수이다.
# ineq는 '<' 또는 '>'로 구성된 문자열이다.
# eq는 '='또는 '!'로 구성된 문자열이다.

def solution(ineq,eq,n,m):
    answer = 0
    if ineq == '<' and eq == '=':
        if n <= m:
            answer = 1
    elif ineq == '>' and eq == '=':
        if n >= m:
            answer = 1
    elif ineq == '<' and eq == '!':
        if n < m:
            answer = 1
    elif ineq == '>' and eq == '!':
        if n > m:
            answer = 1
    else:
        answer = 0

    return answer

ineq,eq,n,m = '<','=',20,50

print(solution(ineq,eq,n,m)) # 1