# 선발고사 등수가 감긴 정수 rank배열과 참여가는 여부가 담긴 boolean 배열 attendance가 주어질 때, 선발학생의 번호가 10000 * a + 100 * b + c를 return하는 함수를 작성하시오.
# 제한사항
# 선발 학생은 등수가 높은 3명이다.
# rank와 attendance의 길이는 3 이상 100 이하이다.
# rank[i]는 i번 학생의 선발고사 등수를 나타내며, 공동 등수의 학생은 없다.
# attendance[i]는 i번 학생의 선발고사 참여 가능여부를 나타내며 True면 가능, False면 불가능이다.
# attendance의 원소 중 적어도 3개는 True이다.

def solution(rank, attendance):
    attend = []
    for i in range(len(attendance)):
        if attendance[i]:
            attend.append([rank[i], i])
    attend.sort()
    print(attend)
    return attend[0][1] * 10000 + attend[1][1] * 100 + attend[2][1]

q1_rank = [3, 7, 2, 5, 4, 6, 1]
q1_attendance = [False, True, True, True, True, False, False]
q2_rank = [6, 1, 5, 2, 3, 4]
q2_attendance = [True, False, True, False, False, True]

print(solution(q1_rank, q1_attendance)) # 20403
print(solution(q2_rank, q2_attendance)) # 50200