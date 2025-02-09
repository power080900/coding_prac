# [x1,y1], [x2,y2], [x3,y3], [x4,y4]가 담겨있는 매개변수 dots가 주어질 때, 직사각형의 넓이를 return하는 함수를 작성하시오.
# 제한사항
# dots의 길이는 4이다
# dots의 각 원소는 [x,y]이다
# dots[i]는 -256 초과 256 미만이다

def solution(dots):
    dots.sort()
    l1 = abs(dots[0][1]-dots[1][1])
    l2 = abs(dots[1][0]-dots[2][0])
    return l1 * l2

q1 = [[1,1],[2,1],[2,2],[1,2]]
q2 = [[-1,-1],[1,1],[1,-1],[-1,1]]

print(solution(q1)) # 1
print(solution(q2)) # 4