# 사과의 최대점수 k, 한 상자당 들어가는 사과의수 m, 각 사과의 점수 score가 주어질 때,
# 과일장수가 얻을 수 있는 최대 이익을 return하는 함수를 작성하시오
# 제한사항
# 한 상자에 담긴 사과들 중 가장 낮은 점수가 p(1<=p<=k)인 경우 사과 한 상자의 가격은 p*m이다.
# k는 3 이상 9 이하의 자연수이다.
# m은 3 이상 10 이하의 자연수이다.
# score의 길이는 7 이상 1,000,000 이하이다.
# score의 각 원소는 1 이상 k 이하의 자연수이다.
# 이익이 없는 경우 0을 return한다.

def solution(k, m, score):
    answer = 0
    box = []
    score.sort(reverse=True)
    for i in range((len(score)//m)*m):
        box.append(score[i])
        if len(box) == m:
            answer += min(box) * m
            box = []
    return answer

q1_k = 3
q1_m = 4
q1_score = [1, 2, 3, 1, 2, 3, 1]

q2_k = 4
q2_m = 3
q2_score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]


print(solution(q1_k, q1_m, q1_score)) # 8
print(solution(q2_k, q2_m, q2_score)) # 33