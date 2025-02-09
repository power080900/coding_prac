# 2자리 이상의 정수 number가 주어질 때 이 수를 2자리씩 자른 뒤, 자른 수를 모두 더해서 그 합을 출력하는 코드를 작성하시오
# 제한사항
# number 은 10 이상 2,000,000,000 이하의 자연수이다.
# number의 자릿수는 2의 배수이다.

def solution(number):
    answer = 0
    for i in range(len(str(number))):
        answer += number  % 100
        number //= 100
    return answer

print(solution(12345678)) # 180