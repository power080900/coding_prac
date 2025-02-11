# 자연수 n이 매개변수로 주어질 때 n의 소인수를 오름차순으로 담은 배열을 return하는 함수를 작성하시오.
# 제한사항
# n은 2 이상 10,000이하의 자연수이다.

def solution(n):
    answer = []
    factor = 2
    while (factor**2 <= n):
        while n % factor == 0:
            answer.append(factor)
            n //= factor
        factor += 1
    if n > 1:
        answer.append(n)
    answer = list(set(answer))
    answer.sort()
    return answer

n = 12

print(solution(n)) # [2,3]
