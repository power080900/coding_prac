# 정수 M,N이 매개변수로 주어질때 1*1 크기로 자를때 필요한 최소한의 가위질 횟수를 return하는 함수를 작성하시오.
# 제한사항
# M,N은 1 이상 99 이하의 자연수이다.
# 종이를 겹쳐서 자를 수는 없다.

def solution(M, N):
    return M*N - 1

q1_M = 2
q1_N = 2
q2_M = 2
q2_N = 5

print(solution(q1_M, q1_N)) # 3
print(solution(q2_M, q2_N)) # 9