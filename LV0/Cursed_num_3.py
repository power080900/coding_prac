# 정수 n이 매개변수로 주어질 때, n이 3의 배수 이거나 3이 들어가면 건너뛰고 그 다음숫자가 return 되는 함수를 작성하시오.
# 제한사항
# n은 1 이상 100 이하인 정수이다.

def solution(n):
    answer = [i for i in range(1, ((3*n)+1))]
    for i in range(1, 3*n):
        if "3" in str(i) or i % 3 == 0:
            answer.remove(i)
    return answer[n-1]

print(solution(15)) # 25
print(solution(40)) # 76