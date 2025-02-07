# 선분 3개가 lines의 매개변수안에 [[start1, end1], [start2, end2], [start3, end3]]으로 주어질 때, 선분이 겹치는 길이를 return하는 함수를 작성하라.
# 제한 사항
# lines의 길이는 3이다.
# lines의 원소의 길이는 2이다.
# 모든 선분은 길이가 1 이상이다.
# lines의 원소는 [start, end] 형식이며 start, end는 1 이상 100 이하인 자연수이고 선분의 시작점과 끝점을 의미한다.

def solution(lines):
    a1 = [i for i in range(min(lines[0]), max(lines[0]))]
    a2 = [i for i in range(min(lines[1]), max(lines[1]))]
    a3 = [i for i in range(min(lines[2]), max(lines[2]))]
    it1 = list(set(a1) & set(a2))
    it2 = list(set(a2) & set(a3))
    it3 = list(set(a1) & set(a3))
    it4 = list(set(a1) & set(a2) & set(a3))
    return len(it1) + len(it2) + len(it3) - len(it4)*2

print(solution([[0, 1], [2, 5], [3, 9]])) # 2