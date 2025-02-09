# 수학점수와 영어점수를 담은 2차원 정수 배열 score가 주어질 때 두 점수의 평균을 기준으로 매긴 등수를 담은 배열을 return하는 함수를 작성하시오.
# score[i]는 0 이상 100 이하이다.
# score의 길이는 1 이상 10 이하이다.
# score의 원소의 길이는 2이며 중복된 원소를 갖지 않는다.

from statistics import mean

def solution(score):
    answer = []
    mean_score = []
    for i in score:
        mean_score.append(mean(i))
    mean_v2 = sorted(mean_score, reverse=True)
    for i in mean_score:
        answer.append(mean_v2.index(i)+1)
    return answer

q1 = [[80, 70], [90, 50], [40, 70], [50, 80]]
q2 = [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]

print(solution(q1)) # [1, 2, 4, 3]
print(solution(q2)) # [4, 4, 6, 2, 2, 1, 7]