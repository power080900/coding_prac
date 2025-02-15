# 전체 학생수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때,
# 체육수업을 들을 수 있는 학생의 최댓값을 return 하는 함수를 작성하시오
# 제한사항
# 전체 학생은 2 이상 30 이하이다.
# 체육복을 도난당한 학생은 1 이상 n 이하이다.
# 여벌의 체육복을 가져온 학생은 1 이상 n 이하이다.
# 여벌의 체육복을 가져온 학생이 체육복을 도난당했을 수 있다.
# 체육복을 1벌만 도난당했을 수 있다.
# 여벌체육복이 있어야 빌려줄 수 있다.

def solution(n, lost, reserve):
    mate = [1 for i in range(1, n+1)]
    inter = set(lost) & set(reserve)
    lost.sort()
    lost = list(set(lost) - inter)
    reserve.sort()
    reserve = list(set(reserve) - inter)
    result = []
    for index, n in enumerate(mate):
        if (index + 1) in lost:
            if (index) in reserve:
                reserve.remove(index)
            elif (index+2) in reserve:
                reserve.remove(index+2)
            else:
                n -= 1
        result.append(n)
    return result.count(1)

q1_n = 5
q1_lost = [2,4]
q1_reserve = [1,3,5]
q2_n = 5
q2_lost = [2,4]
q2_reserve = [3]
q3_n = 3
q3_lost = [3]
q3_reserve = [1]

print(solution(q1_n, q1_lost, q1_reserve)) # 5
print(solution(q2_n, q2_lost, q2_reserve)) # 4
print(solution(q3_n, q3_lost, q3_reserve)) # 2