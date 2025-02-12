# 정수 n과 2차원 정수 배열 q와 1차원 정수배열 ans가 매개변수로 주어질때 비밀코드로 가능한 정수 조합개수를 return하도록 함수를 작성하시오.
# 제한사항
# 암호분석 코드를 사용하여 m번의 시도를 할 수 있다.
# n은 10 이상 30 이하이다.
# q의 길이와 m은 동일하며 1 이상 10 이하이다.
# q[i]의 길이는 5이다.
# q[i]는 i+1번째 시도에서 입력한 5개의 정수 중 비밀코드에 포함된 정수의 개수를 나타낸다.
# ans[i]는 0 이상 5 이하이다.
# 비밀코드가 존재하지 않는 경우는 없다.

from itertools import combinations


def solution(n, q, ans):
    answer = 0
    
    for j in list(combinations(range(1, n+1), 5)):
        for k in q:
            if len(set(j) & set(k)) != ans[q.index(k)]:
                break
        else:
            answer += 1
    return answer

q1_n = 10
q1_q = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]]
q1_ans = [2, 3, 4, 3, 3]
q2_n = 15
q2_q = [[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]]
q2_ans = [2, 1, 3, 0, 1]

print(solution(q1_n, q1_q, q1_ans)) # 3
print(solution(q2_n, q2_q, q2_ans)) # 5